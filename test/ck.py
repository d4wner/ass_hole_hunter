#!/usr/bin/env python
#coding=utf-8

import cookielib
import urllib2
import re

cj =  cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
f = opener.open("http://192.168.1.101/dedecms///dede/login.php")
html = f.read()
#cj = cookielib.Cookiejar()
#for index, cookie in enumerate(cj):
for cookie in cj:
    ck = str(cookie)
print ck
session = re.search(r'=.*\sf',ck).group(0)[1:-2]
print session
