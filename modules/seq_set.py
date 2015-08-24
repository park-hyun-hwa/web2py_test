#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
from gluon.globals import *

def seq_init():
    db = current.db
    if db(db.phh_order.phh_order_name == 'number').isempty() :
        db.phh_order.insert(phh_order_name='number',phh_order_value='0')
        db.phh_order.insert(phh_order_name='lock',phh_order_value='False')
        db.commit()
    else :
        db(db.phh_order.phh_order_name == 'number').update(phh_order_value='0')
        db(db.phh_order.phh_order_name == 'lock').update(phh_order_value='False')
        db.commit()
    
def seq_getting():
    db = current.db
    num_row=db(db.phh_order.phh_order_name =='number').select().first()
    seq_num=num_row.phh_order_value
    print "seq_get : %s" %seq_num
    return seq_num

def seq_setting(number):
    db = current.db
    db(db.phh_order.phh_order_name == 'number').update(phh_order_value=number)
    num_row=db(db.phh_order.phh_order_name =='number').select().first()
    seq_num=num_row.phh_order_value
    db.commit()
    print "seq_set: %s" %seq_num
    
def lock_getting():
    db = current.db
    lock_row=db(db.phh_order.phh_order_name =='lock').select().first()
    is_lock = lock_row.phh_order_value
    print "lock:%s" %is_lock
    return is_lock

def lock_setting(state):
    db = current.db
    db(db.phh_order.phh_order_name == 'lock').update(phh_order_value=state)
    lock_row=db(db.phh_order.phh_order_name =='lock').select().first()
    is_lock = lock_row.phh_order_value
    db.commit()
    print "lock_set:%s" %is_lock
