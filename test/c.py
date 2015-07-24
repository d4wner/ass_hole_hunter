import httplib
import urllib
from bs4 import BeautifulSoup

print "=================================================="
print "==============ContructionSiteQuery================"
print "=================================================="
input_url=raw_input("please input url:")
httpclient = httplib.HTTPConnection("tool.chinaz.com")
params = urllib.urlencode({"s":input_url})
headers = {"Host":"s.tool.chinaz.com",
         "Origin":"http://s.tool.chinaz.com/",
         "Referer":"http://s.tool.chinaz.com/",
         "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36",
         "Connection":"keep-alive",
         "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
         "Content-Type":"application/x-www-form-urlencoded"}
httpclient.request("POST", "/Same", params , headers)
response = httpclient.getresponse();

content= response.read()
soup = BeautifulSoup(''.join(content))
els=soup.find_all(id="contenthtml")
for item in els:
    for child in item.children:
        if(len(child)==1) :
            continue
        for ul in child.children :
            for ul_c in ul:
                str=ul_c.string
                if(len(str)>4):
                    print str
raw_input("==============END================")
