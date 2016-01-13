#coding:utf-8
import urllib,urllib2,cookielib


bgp_he_dns = "http://bgp.he.net/dns/www.bstaint.net/#_dns"

cj = cookielib.LWPCookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux i686; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.2.0'),('referer','http://bgp.he.net')]
req = urllib2.Request(bgp_he_dns)
resp = opener.open(req).read()

conn = urllib2.urlopen(req)
resp = conn.geturl()

#resp = opener.open(req).read()

print resp

