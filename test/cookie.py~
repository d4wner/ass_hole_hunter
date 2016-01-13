#coding:utf-8
import urllib,urllib2,cookielib

cj = cookielib.LWPCookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
login_path = 'http://192.168.1.101/dedecms///dede/login.php'

request = urllib2.Request(login_path)
html = opener.open(request).read()
if cj:
    print cj
for index, cookie in enumerate(cj):
    print cookie
