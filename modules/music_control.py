#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
import pygame
import time

def music_init():
    pygame.mixer.init()
    
def music_start(filename):
    if pygame.mixer.get_init():
        pygame.mixer.music.fadeout(5000)
        time.sleep(3)
    
    pygame.mixer.music.load("/home/pi/hyunhwa/web2py/applications/test/static/%s"%filename)
    pygame.mixer.music.play()

def music_stop():
    pygame.mixer.music.fadeout(5000)
    
def music_repeat():
    pygame.mixer.music.play(-1,0.0)
