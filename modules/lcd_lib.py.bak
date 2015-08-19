#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
import RPi.GPIO as GPIO
import time, os
from subprocess import *
from lcd_connect import *
#import GPIOClient as GPIO

# Define GPIO to LCD mapping, Raspi pin mapping
LCD_RS = 6 # LCD pin 4 : RS (Register Select)
LCD_E  = 13 # LCD pin 6 : Enable or Strobe
LCD_D4 = 19 # LCD pin 11: Data Bit 4
LCD_D5 = 26 # LCD pin 12: Data Bit 5
LCD_D6 = 21 # LCD pin 13: Data Bit 6

LCD_D7 = 20 # LCD pin 14: Data Bit 7
LCD_RED = 16 # LCD pin 16: RED LCD Backlight (-)
LCD_GREEN = 12 # LCD pin 17: GREEN LCD Backlight (-)
LCD_BLUE = 7 # # LCD pin 18: BLUE LCD Backlight (-)

# Define some device constants
LCD_WIDTH = 16    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

def lcd_init():
    print 'init'
    GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
    GPIO.setup(LCD_E, GPIO.OUT)  # E
    GPIO.setup(LCD_RS, GPIO.OUT) # RS
    GPIO.setup(LCD_D4, GPIO.OUT) # DB4
    GPIO.setup(LCD_D5, GPIO.OUT) # DB5
    GPIO.setup(LCD_D6, GPIO.OUT) # DB6
    GPIO.setup(LCD_D7, GPIO.OUT) # DB7
    #GPIO.setup(LED_ON, GPIO.OUT) # Backlight enable
    GPIO.setup(LCD_RED, GPIO.OUT) # RED Backlight enable
    GPIO.setup(LCD_GREEN, GPIO.OUT) # GREEN Backlight enable
    GPIO.setup(LCD_BLUE, GPIO.OUT) # BLUEBacklight enable

    # Initialise display
    lcd_byte(0x33,LCD_CMD) # 110011 Initialise
    lcd_byte(0x32,LCD_CMD) # 110010 Initialise
    lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
    lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off
    lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
    lcd_byte(0x01,LCD_CMD) # 000001 Clear display
    time.sleep(E_DELAY)

def lcd_clear():
    lcd_byte(0x01,LCD_CMD) # 000001 Clear display
    time.sleep(E_DELAY)

def lcd_byte(bits, mode):
    # Send byte to data pins
    # bits = data
    # mode = True  for character
    #        False for command
    GPIO.output(LCD_RS, mode) # RS
    # High bits
    GPIO.output(LCD_D4, False)
    GPIO.output(LCD_D5, False)
    GPIO.output(LCD_D6, False)
    GPIO.output(LCD_D7, False)
    if bits&0x10==0x10: GPIO.output(LCD_D4, True)
    if bits&0x20==0x20: GPIO.output(LCD_D5, True)
    if bits&0x40==0x40: GPIO.output(LCD_D6, True)
    if bits&0x80==0x80: GPIO.output(LCD_D7, True)
    # Toggle 'Enable' pin
    lcd_toggle_enable()
    # Low bits
    GPIO.output(LCD_D4, False)
    GPIO.output(LCD_D5, False)
    GPIO.output(LCD_D6, False)
    GPIO.output(LCD_D7, False)
    if bits&0x01==0x01: GPIO.output(LCD_D4, True)
    if bits&0x02==0x02: GPIO.output(LCD_D5, True)
    if bits&0x04==0x04: GPIO.output(LCD_D6, True)
    if bits&0x08==0x08: GPIO.output(LCD_D7, True)
    # Toggle 'Enable' pin
    lcd_toggle_enable()

def lcd_toggle_enable():
    # Toggle enable
    time.sleep(E_DELAY)
    GPIO.output(LCD_E, True)
    time.sleep(E_PULSE)
    GPIO.output(LCD_E, False)
    time.sleep(E_DELAY)

def lcd_string(message,line,style):
    # Send string to display
    # style=1 Left justified
    # style=2 Centred
    # style=3 Right justified
    if style==1:
        message = message.ljust(LCD_WIDTH," ")
    elif style==2:
        message = message.center(LCD_WIDTH," ")
    elif style==3:
        message = message.rjust(LCD_WIDTH," ")

    lcd_byte(line, LCD_CMD)

    for i in range(LCD_WIDTH):
        lcd_byte(ord(message[i]),LCD_CHR)

def redLCDon():
    red_backlight(False)

def greenLCDon():
    green_backlight(False)

def blueLCDon():
    blue_backlight(False)

def LCDoff():
    red_backlight(True)
    green_backlight(True)
    blue_backlight(True)

def yellowLCDon():
    GPIO.output(LCD_BLUE, True)
    GPIO.output(LCD_RED, False)
    GPIO.output(LCD_GREEN, False)

def skyeLCDon():
    GPIO.output(LCD_BLUE, True)
    GPIO.output(LCD_RED, False)
    GPIO.output(LCD_GREEN, False)

def pinkLCDon():
    GPIO.output(LCD_GREEN, True)
    GPIO.output(LCD_RED, False)
    GPIO.output(LCD_BLUE, False)

def whiteLCDon():
    GPIO.output(LCD_RED, False)
    GPIO.output(LCD_GREEN, False)
    GPIO.output(LCD_BLUE, False)

def red_backlight(flag):
    # Toggle red-backlight on-off-on
    GPIO.output(LCD_GREEN, True)
    GPIO.output(LCD_BLUE, True)
    GPIO.output(LCD_RED, flag)

def green_backlight(flag):
    # Toggle green-backlight on-off-on
    GPIO.output(LCD_RED, True)
    GPIO.output(LCD_BLUE, True)
    GPIO.output(LCD_GREEN, flag)

def blue_backlight(flag):
    # Toggle blue-backlight on-off-on
    GPIO.output(LCD_RED, True)
    GPIO.output(LCD_GREEN, True)
    GPIO.output(LCD_BLUE, flag)

def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output
