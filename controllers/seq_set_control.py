# -*- coding: utf-8 -*-
# try something like

from gluon import *
from gluon.globals import *

global sequence
global lock
sequence = 2
lock = False

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

def seq_setting(value):
    global sequence
    sequence=value
    print "seq_set : %s" %sequence
    return sequence
    
def lock_getting():
    global lock
    print "lock_get:%s" %lock
    return lock

def lock_setting(value):
    global lock
    lock=value
    print "lock_set:%s" %lock
    return lock
