#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
import smbus
import time
import sys
import datetime
from lcd_lib import *


LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line

SHT20_ADDR = 0x40       # SHT20 register address
SHT20_CMD_R_T = 0xF3    # no hold Master Mode (Temperature)
SHT20_CMD_R_RH = 0xF5   # no hold Master Mode (Humidity)
SHT20_CMD_RESET = 0xFE  # soft reset

bus = smbus.SMBus(1)    # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)

def reading(v):
    #bus.write_quick(SHT20_ADDR)
    if v == 1:
        bus.write_byte(SHT20_ADDR, SHT20_CMD_R_T)
    elif v == 2:
        bus.write_byte(SHT20_ADDR, SHT20_CMD_R_RH)
    else:
        return False
        
    time.sleep(.1)
    
    b = (bus.read_byte(SHT20_ADDR)<<8)
    b += bus.read_byte(SHT20_ADDR)
    return b

def calc(temp, humi):
    tmp_temp = -46.85 + 175.72 * float(temp) / pow(2,16)
    tmp_humi = -6 + 125 * float(humi) / pow(2,16)

    return tmp_temp, tmp_humi

def sht_db_main(v):
    now = datetime.datetime.now()
    temp = reading(1)
    humi = reading(2)
    if not temp or not humi:
        print "register error"
        #break
    value = calc(temp, humi)
    result="temp:"+str(value[0])+"\t humi:"+str(value[1])
    if v==1:
        return round(value[0], 3)
    elif v==2:
        return round(value[1], 3)
    else:
        return False
def main():
        #data=open('sht20_data.txt','w')
        temp = reading(1)
        humi = reading(2)
        if not temp or not humi:
            print "register error"
            #break
        value = calc(temp, humi)
        result="temp:"+str(value[0])+"\t humi:"+str(value[1])
        print "%s" %(result)
        lcd_string('temp : %s' %(value[0]),LCD_LINE_1,1)
        lcd_string('humi : %s' % (value[1]),LCD_LINE_2,1)
        time.sleep(2)
