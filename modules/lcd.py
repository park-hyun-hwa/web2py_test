#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
from lcd_lib import *
from seq_set import *

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line

def flow_lcd(line1_str,line2_str):

    dif1 = len(line1_str)-16
    dif2 = len(line2_str)-16
    if dif1>=dif2:
        print 'flow'
        for i in range(dif1+2) :
            fin_line1_str = line1_str[i:i+15]
            fin_line2_str = line2_str[i:i+15]
            lcd_string('%s' %(fin_line1_str),LCD_LINE_1,1)
            lcd_string('%s' % (fin_line2_str),LCD_LINE_2,1)
            time.sleep(1)
    else :
    	for i in range(dif2+2) :
            fin_line1_str = line1_str[i:i+15]
            fin_line2_str = line2_str[i:i+15]
            lcd_string('%s' %(fin_line1_str),LCD_LINE_1,1)
            lcd_string('%s' % (fin_line2_str),LCD_LINE_2,1)
            time.sleep(1)

def alert_lcd(num):
    seq_getting()
    seq_setting(1)
    lcd_init()
    if lock_getting()==False:
        lock_setting(True)
        if num == '1':
            time.sleep(1)
            flow_lcd('Temperature too high','Turn on Fan')
            redLCDon()
        elif num == '2':
            time.sleep(1)
            flow_lcd('Humidity too high','Turn on Air conditioning')
            blueLCDon()
        elif num == '3':
            time.sleep(1)
            flow_lcd('Dust too high','Close the windows')
            yellowLCDon()
        elif num == '4':
            time.sleep(1)
            flow_lcd('CO2 too high','Open the windows')
            pinkLCDon()
        lock_setting(False)
        seq_getting()
        seq_setting(0)
    else :
        while lock_getting()==True:
            time.sleep(3)
        lock_setting(True)
        if num == '1':
            time.sleep(1)
            flow_lcd('Temperature too high','Turn on Fan')
            redLCDon()
        elif num == '2':
            time.sleep(1)
            flow_lcd('Humidity too high','Turn on Air conditioning')
            blueLCDon()
        elif num == '3':
            time.sleep(1)
            flow_lcd('Dust too high','Close the windows')
            yellowLCDon()
        elif num == '4':
            time.sleep(1)
            flow_lcd('CO2 too high','Open the windows')
            pinkLCDon()
        lock_setting(False)