# -*- coding: utf-8 -*-
# try something like
from gluon import *
from gluon.globals import *


sequence = '2'
lock = 'False'

def seq_init():
    global sequence
    global lock
    sequence = '0'
    lock = 'False'
    return True

def seq_getting():
    global sequence
    print "seq_get : %s" %sequence
    return sequence

def seq_setting():
    global sequence
    sequence=request.vars.value
    print "seq_set : %s" %sequence
    return sequence
    
def lock_getting():
    global lock
    print "lock_get:%s" %lock
    return lock

def lock_setting():
    global lock
    lock=request.args(0)
    print "lock_set:%s" %lock
    return lock
