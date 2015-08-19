#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
import serial,os,time
import sys
import RPi.GPIO as GPIO
#import logging
#import logging.handlers

import json
import requests
import fcntl, socket, struct

DEBUG_PRINT = 1
SERIAL_READ_BYTE = 12


sensorname = "co2.test"

def checkAlignment(incoming):
    idxNum = incoming.find('m')
    # idxNum is 9, correct
    offset = idxNum - 9 
    if offset > 0 :
        new_str = incoming[offset:]
        new_str = new_str + incoming[:offset]
    if offset < 0 :
        offset = 12 + offset 
        new_str = incoming[offset:]
        new_str = new_str + incoming[:offset]
    return new_str
    
def CO2(num):
    ppm = 0 
    print 'ddd'
    serial_in_device = serial.Serial('/dev/ttyAMA0',38400)
    in_byte = serial_in_device.read(SERIAL_READ_BYTE)
    
    pos = 0
    print 'eeee'
    if not (len(in_byte) is SERIAL_READ_BYTE) : 
        return -1
    # sometimes, 12 byte alighn is in-correct
    # espacially run on /etc/rc.local
    if not in_byte[9] is 'm':
        shift_byte = checkAlignment(in_byte)
        in_byte = shift_byte
    if ('ppm' in in_byte):
        if not(in_byte[2] is ' ') :
            ppm += (int(in_byte[2])) * 1000
        if not (in_byte[3] is ' ') :
            ppm += (int(in_byte[3])) * 100
        if not (in_byte[4] is ' ') :
            ppm += (int(in_byte[4])) * 10
        if not (in_byte[5] is ' ') :
            ppm += (int(in_byte[5]))
    print ppm
    
        
    return ppm
