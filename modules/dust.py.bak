#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
import os
import sys
import urllib2
import httplib
import time
import datetime

conn = httplib.HTTPConnection("192.168.0.16")
data =''
co2 = ''

def getDatablocks(buffers):
    a = buffers.split('<tbody id="mt_mmc2_10007">')[1]
    b = a.split('</tbody>')[0].replace('<tr>','').replace('</tr>','').replace('</td>','')
    r = ''
    value=[]

    for line in b.split('<td>'):
        if len(line) < 30:
            line = line.strip()
            r = r+line+' '
        else:
            line = line.strip()
            r = r+line+'\n'
            value.append(line)
    return value

def get_page():
    page = urllib2.urlopen("http://www.airkorea.or.kr/index")
    text = page.read()
    return text

def print_dust(value):
    print "seoul : "+value[1]
    print "busan : "+value[2]
    print "deagu : "+value[3]
    print "incheon : "+value[4]
    print "gwangju : "+value[5]
    print "daejeon : "+value[6]

def dust_info(num):
    buffers = get_page()
    #current_time = getDatetime(buffers)
    dust = getDatablocks(buffers)
    return dust[num]
