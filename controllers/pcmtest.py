# -*- coding: utf-8 -*-
# try something like

from gluon import *

global pcm_var
pcm_var = 0

def set_pcm(pcm):
    global pcm_var
    pcm_var = pcm
    
def get_pcm():
    global pcm_var
    return pcm_var
