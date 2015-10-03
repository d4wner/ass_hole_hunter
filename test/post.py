#!/usr/bin/env python
#coding=utf-8
import urllib
import urllib2

value = ''
url  = 'http://192.168.1.101/dedecms/data/sessions/sess_841680864765fe40dbc9dbf4346dd856'
data = urllib.urlencode(value)
headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/31.0.1271.64 Safari/537.11' }
if value == "": 
    res = urllib2.Request(url,headers = headers)
else:
    res = urllib2.Request(url,data,headers)
try:
    resp = urllib2.urlopen(res)
except Exception,e:
    print e
    resp = None
#return resp


