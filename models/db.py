db = DAL('sqlite://storage.sqlite',
        pool_size=1, check_reserved=['all'],
        migrate_enabled=True, lazy_tables=True)

from gluon.tools import Auth
from gluon import current
auth = Auth(db)

auth.define_tables(username=False, signature=False)

auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

#current.sequence = 2 #0:background,1:alert by LCD,2:lock,3:unlock
#current.lock = False
current.db=db
db.define_table('chat',
        Field('me_from'),
        Field('me_body', 'text'),
        Field('me_html', 'text'),
        )
db.define_table('sht20',
                Field('data_time',requires=IS_NOT_EMPTY()),
                Field('temperature'),
                Field('humidity'),
                Field('co2'))
db.define_table('phh_order',
                Field('phh_order_name'),
                Field('phh_order_value'))
db.define_table('play_list',
                Field('song_name'))
db.play_list.song_name.requires=IS_IN_SET(('sound_test.mp3','alarm.mp3','huhgak.mp3','love.mp3'))
