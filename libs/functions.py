#!/usr/bin/env python
#coding=utf-8

#from libs.Threads import ThreadPool
#from libs.color import *
#import libs.socks as socks


import urllib2
import urllib
import httplib
import random
import time
import re
import os
import sys
import requests
import sqlite3
import socket
import base64
import cookielib
import datetime
import urlparse

sys.path.append('dbs/')
sys.path.append('modules')

from bs4 import BeautifulSoup
from libs.Threads import ThreadPool
from config import global_config
from path_scan import  hunter_plugin

#from config import global_config

def url_head(url):
    try:
        resp = req.head(url)
    except KeyboardInterrupt:
        raise
    except Exception,e:
        resp = None
    return resp

def url_get(url):
    return urllib2.urlopen(url)

def url_Get(req,url,**kwargs):
    """ 
    HTTP GET REQUESTS.
    """
    try:
        resp = req.get(url,**kwargs)

    except KeyboardInterrupt:
        raise

    except Exception, e:
        resp = None
    return resp

def url_Head(url,path,port):
    conn = httplib.HTTPConnection(url) 
    conn.request("HEAD",port,"/"+path)
    resp = conn.getresponse()
    return resp



def url_post(url,value=""):
    try:
        data = urllib.urlencode(value)
    except:
        data = urllib.quote_plus(value)
    print data
    headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/31.0.1271.64 Safari/537.11' }
    if value == "":
        res = urllib2.Request(url,headers = headers)
    else:
        res = urllib2.Request(url,data = data ,headers = headers)
    try:
        resp = urllib2.urlopen(res)
    except Exception,e:
        print e
        resp = None
    return resp

def url_upload(url,value):
    cookies = cookielib.CookieJar()
    opener  = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies),MultipartPostHandler.MultipartPostHandler)
    opener.open(url, value)

def url_proxy(url,port_type):
    if port_type=="http":
        proxy_port = xxx
    else:
        proxy_port = xxx    
    conn = httplib.HTTPConnection(proxy_host, proxy_port)
    resp = conn.getresponse()
    if resp.status == 200:
        resp = resp.read()
    else:
        resp = None
    return resp

def result_write():
    result = global_config.infos['result_path']+'/report.txt'
    r = open(result,'a+')
    return r


def key_find(url,value):
    return re.findall(url,value)


def run_payload(payload,arr):
    if len(payload) > 0 and payload != None:
        color.echo("Start exploit...",RED)
        #code=open("modules/"+payload+".py").read()
        #exec(code)
        #module_path = os.path.join("modules",payload+".py")
        #sys.path.append(module_path)
        #plugin_info, resp = 
        plugin=__import__("modules."+payload, fromlist=[payload])
        plugin.exploit(arr)

def log_record(msg,msg_type=""):
    #e means error here...
    if msg_type == "e":
        e_msg = "[x]"+msg+"\n"
        print e_msg
        e = open("result/error.log","a+")
        e.writelines(e_msg)
        e.close()

    #s means success here...
    elif msg_type == "s":
        s_msg =  "[!]"+msg+"\n"
        print s_msg
        s = open("result/success.log","a+")
        s.writelines(s_msg)
        s.close()
    elif msg_type == "":
        print "[+]"+msg+"\n"



def logo_print():
    print """
+-----------------------------+
|                             |
|     Ass-Hole-Hunter v1.0    |
|       Code by demon         |
|                             |
+-----------------------------+
    """



