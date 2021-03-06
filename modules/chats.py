# -*- coding: utf-8
from gevent.event import Event

from gluon.template import render
from gluon.dal import Field
from gluon.globals import current
from gluon.serializers import *

from sht_db import *
from dust import *
from co2 import *
from lcd import alert_lcd,message_alert

new_message_event = Event()

MESSAGE_TEMPLATE = ("""<div class="message" id="m{{ =message['id'] }}">""" """<b>{{ =message['me_from'] }}: </b>""" """<pre>{{ =message['me_body'] }}</pre></div>""")

def _create_message(db, from_, body):
    data = {'me_from': from_, 'me_body': body}
    mid = db.chat.insert(**data)
    data['id'] = str(mid)
    if current.session.auth.user.first_name == from_ :
        MESSAGE_TEMPLATE = ("""<div style="text-align:right" class="message" id="m{{ =message['id'] }}">""" """<b>{{ =message['me_from'] }}: </b>""" """<pre>{{ =message['me_body'] }}</pre></div>""")
    else:
        MESSAGE_TEMPLATE = ("""<div style="text-align:left" class="message" id="m{{ =message['id'] }}">""" """<b>{{ =message['me_from'] }}: </b>""" """<pre>{{ =message['me_body'] }}</pre></div>""")
    
    data['me_html'] = render(MESSAGE_TEMPLATE, context={'message': data})
    db(db.chat.id == mid).update(me_html=data['me_html'])
    return data


# main page that renders the chat
def index(db):
    chat_set = db(db.chat.id > 0)
    # how many messages do we have?
    n = chat_set.count()
    # get the last ten
    rows = chat_set.select(limitby=(n - 10, 10))
    # save in session the last seen message id
    current.session.cursor = rows.last().id if rows else 0
    return dict(messages=rows)


# Ajax call bellow.
# When the index above is rendered it will display
# the last 10 messages and then makes an ajax request
# to `message_updates` function

# A new message arrived. The new message is created and
# everyone that is waiting (new_message_event.wait()) is awake
# with a signal (new_message_event.set())
def message_new(db):
    name = current.session.auth.user.first_name

    body = current.request.vars.body
    if body == "show state" :
        msg = _create_message(db, name, body)
        _create_message(db, 'temperature', "현재 온도는 "+str(sht_db_main(1))+" ℃ 입니다.")
        _create_message(db, 'humidity', "현재 습도는 "+str(sht_db_main(2))+" ％ 입니다.")
        _create_message(db, 'dust', "현재 서울의 미세먼지 농도는 "+str(dust_info(1))+" ％ 입니다.")
        _create_message(db, 'co2', "현재 co2 농도는 "+str(CO2(1))+" ppm 입니다.")
    elif "alert by LCD" in body:
        msg = _create_message(db, name, body)
        value=body.split('/')
        alert_lcd(value[1])
    elif "send message" in body:
        print "send message"
        msg = _create_message(db,name,body)
        value = body.split('/')
        print "%s" %value[1]
        message_alert(name,value[1])
    else :
        msg = _create_message(db, name, body)
    new_message_event.set()
    new_message_event.clear()
    return msg


# this will hold the request if there is no new messages
# as soon as a there is a new message the request is finished
# and returns the new message to clients that were waiting.
def message_updates(db):
    cursor = int(current.session.cursor or 0)
    q = db.chat.id > cursor
    rows = db(q).select()
    if not rows:
        new_message_event.wait()
        rows = db(q).select()
    
    if rows:  # This should be always True
        current.session.cursor = rows.last().id
        #return json({'messages': rows.as_list()})
        return index(db)
    # Should never happen. Just in case
    return json({'messages': []})
