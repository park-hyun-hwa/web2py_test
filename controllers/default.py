# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

import chats
from sht_db import *
from co2 import *
from datetime import datetime, timedelta
from time import localtime,strftime
import pygame

#from co2 import syncfind,checkAlignment,init_process

def index():
    response.flash = T("Welcome to web2py!")
    return dict(message=T('Hello Hyun Hwa Test Page'))


def user():
    return dict(form=auth())


@cache.action()
def download():
    return response.download(request, db)


def call():
    return service()



def check_form():
    #update = db.register(request.args(0))
    form = SQLFORM(db.client)
    if form.accepts(request,session):
        response.flash = 'Thanks! The form has been submitted.'
    elif form.errors:
       response.flash = 'Please correct the error(s).'
    else:
       response.flash = 'Try again - no fields can be empty.'
    return dict(form=form)

def all_records():
    grid = SQLFORM.grid(db.auth_user,user_signature=False)
    return locals()

def sht_db():
    #db.sht20.insert(data_time=datetime.datetime.now(),temperature=sht_db_main(1),humidity=sht_db_main(2),co2=0)
    #time.sleep(10)
    #grid = SQLFORM.grid(db.sht20,user_signature=False)
    
    #db.chat.insert(data_time=datetime.datetime.now(),temperature=sht_db_main(1),humidity=sht_db_main(2),co2=0)
    #chats._create_message(db,'temperature',sht_db_main(1))
    #chats._create_message(db,'humidity',sht_db_main(2))
    grid = SQLFORM.grid(db.chat,user_signature=False)
    return locals()
   

@auth.requires_login()
def chatting():
    return chats.index(db)

#@auth.requires_signature()
def message_new():
    return chats.message_new(db)

@auth.requires_signature()
def message_updates():
    # need to unlock the session when using
    # session file, should not be need it when
    # using session in db, or in a cookie
    session._unlock(response)
    return chats.message_updates(db)

#@auth.requires_signature()
def sensor_updates():
    #chats._create_message(db, 'temperature', "현재 온도는 "+str(sht_db_main(1))+" ℃ 입니다.")
    #chats._create_message(db, 'humidity', "현재 습도는 "+str(sht_db_main(2))+" ％ 입니다.")
    if sht_db_main(1)>28:
        chats._create_message(db, 'temperature', "현재 온도는 "+str(sht_db_main(1))+" ℃ 입니다.\n온도가 너무 높습니다.\n명령 : alert by LCD/1")
    elif sht_db_main(2)>70:
        chats._create_message(db, 'humidity', "현재 습도는 "+str(sht_db_main(2))+" ％ 입니다.\n습도가 너무 높습니다. \n명령 : alert by LCD/2")
    else :
        chats._create_message(db, 'none', "쾌적한 상태입니다.")
    return chats.index(db)

def tsdb():
    now = datetime.now()
    timegap = timedelta(hours=3)
    before = now - timegap
    current_time=before.strftime("%Y/%m/%d-%H:%M:%S")
    return dict(time=T(current_time))

def player_control():
    form = SQLFORM(db.play_list)
    if form.vars.song_name is not null:
        if form.accepts(request,session):
            pygame.mixer.init()
            pygame.mixer.music.stop()
            response.flash = 'music stop!!'
            pygame.mixer.music.load("/home/pi/hyunhwa/web2py/applications/test/static/%s"%form.vars.song_name)
            pygame.mixer.music.play()
            response.flash = 'music start!!'
    else :
        response.flash = 'file is not selected'
        
    return dict(form=form)
