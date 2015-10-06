#!/usr/bin/env python
#coding=utf-8

import hashlib
import urllib2
import sys
import requests

url = sys.argv[1]
print url
#resp = urllib2.urlopen(url)
resp = requests.get(url)
md5 = hashlib.md5(resp.content).hexdigest()
print md5
