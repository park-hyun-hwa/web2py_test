#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
from lcd_lib import *
#from seq_set_control import *
from pcmtest import *
import pygame

#from seq_set import *

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
    urllib2.urlopen('https://169.254.1.231:8000/test/seq_set/seq_getting')
    urllib2.urlopen('https://169.254.1.231:8000/test/seq_set/seq_setting/1')
    lcd_init()
    #initialise sound
    pygame.mixer.init()
    pygame.mixer.music.load("/home/pi/hyunhwa/web2py/applications/test/static/alarm.mp3")
    if urllib2.urlopen('https://169.254.1.231:8000/test/seq_set/lock_getting') == 'False':
        urllib2.urlopen('https://169.254.1.231:8000/test/seq_set/lock_setting/True')
        
        pygame.mixer.music.play()
        print "start play"
        
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
        urllib2.urlopen('https://169.254.1.231:8000/test/seq_set/lock_getting')
        urllib2.urlopen('https://169.254.1.231:8000/test/seq_set/lock_setting/False')
        
    else :
        while urllib2.urlopen('https://169.254.1.231:8000/test/seq_set/lock_getting') == 'True':
            time.sleep(3)
        urllib2.urlopen('https://169.254.1.231:8000/test/seq_set/lock_setting/True')

        pygame.mixer.music.play()
        print "start play"
        
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
        urllib2.urlopen('https://169.254.1.231:8000/test/seq_set/lock_getting')
        urllib2.urlopen('https://169.254.1.231:8000/test/seq_set/lock_setting/False')
    urllib2.urlopen('https://169.254.1.231:8000/test/seq_set/seq_getting')
    urllib2.urlopen('https://169.254.1.231:8000/test/seq_set/seq_setting/0')
