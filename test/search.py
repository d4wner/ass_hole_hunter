#!/usr/bin/env python
#coding=utf-8

import httplib
import urllib
import urllib2
from bs4 import BeautifulSoup
import shodan

#input_url=raw_input("please input url:")
#option = raw_input("please choose the source:")
#组合排列过滤？

def chinaz(input_url):
    httpclient = httplib.HTTPConnection("tool.chinaz.com")
    params = urllib.urlencode({"s":input_url})
    headers = {"Host":"s.tool.chinaz.com",
             "Origin":"http://s.tool.chinaz.com/",
             "Referer":"http://s.tool.chinaz.com/",
             "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36",
             "Connection":"keep-alive",
             "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
             "Content-Type":"application/x-www-form-urlencoded"}
    httpclient.request("POST", "/Same?jdfwkey=pbqvo2", params , headers)
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

def aizhan(input_url):
    aizhan_url = 'http://dns.aizhan.com/?q='+input_url
    resp = urllib2.urlopen(aizhan_url).read()
    #print resp
    soup = BeautifulSoup(''.join(resp))
    print type(soup)
    gg01 = soup.find("div", attrs={"class": "gg01"})
    print type(els)
    els = gg01.find_all('a')
    #els=soup.find('div',class_="gg01")
    #print els
    #els=els.find_all('a')
    for item in els:
        print item.text.strip()


def oshadan(input_url):
    count = 1
    while(1):
        oshadan_url = "https://www.oshadan.com/search?c="+input_url+"&p="+str(count)
        resp = urllib2.urlopen(oshadan_url).read()
        if "请登录" in resp:
            break
        soup = BeautifulSoup(''.join(resp))
        result_info_div = soup.find("div", attrs={"id": "result_info_div"})
        title = result_info_div.find_all("div", attrs={"class": "title"})
        if title == None:
            break
        #print title
        for t in title:
            try:
                a = t.find("a")
                print a['href']
            except:
                continue
        count = count + 1
        print "-------------"

#def shodan(input_url):
#    SHODAN_API_KEY = "0dsB7CsdVWVvNBeVG2BUSkrq5Tly0bP7"
#    api = shodan.Shodan(SHODAN_API_KEY)
#         try:
#        # Search Shodan
#        results = api.search('apache')
#
#        # Show the results
#        print 'Results found: %s' % results['total']
#        for result in results['matches']:
#                print 'IP: %s' % result['ip_str']
#                print result['data']
#                print ''
#except shodan.APIError, e:
#        print 'Error: %s' % e    

def bgp_he(input_url):
    bgp_he_url = "http://bgp.he.net/ip/"+input_url+"#_dns"
    print bgp_he_url
    #resp = urllib2.urlopen(bgp_he_url).read()
    req = urllib2.Request(bgp_he_url)
    req.add_header('User-Agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')
    req.add_header('referer','http://bgp.he.net')
    resp= urllib2.urlopen(req).read()
    #if "请登录" in resp:
    #    break
    soup = BeautifulSoup(''.join(resp))
    result_info_div = soup.find("div", attrs={"id": "dns"})
    a_text = result_info_div.find_all("a")
    #if title == None:
    #    break
    #print title
    for item in a_text:
        print item.text

def fofa(input_url):
    count = 1
    while(1):
        fofa_url = 'http://fofa.so/search/result?q=ip%3D"'+input_url+'"'+'&page='+str(count)
        print fofa_url
        #resp = urllib2.urlopen(bgp_he_url).read()
        req = urllib2.Request(fofa_url)
        req.add_header('User-Agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')
        req.add_header('referer','http://fofa.so')
        resp= urllib2.urlopen(req).read()
        #print resp
        #if "请登录" in resp:
        #    break
        soup = BeautifulSoup(''.join(resp))
        result_info_div = soup.find_all("div", attrs={"class": "col-lg-4"})
        print len(result_info_div)
        if len(result_info_div)<2:
            return None
        for div_content in result_info_div[1:]:
            a_text = div_content.find("a")
            print a_text['href']
            
            #if 'qbase64' not in str(div_content):
            #    print '-======'
            #    #print div_content
            #    print '======='
            
            #if 'fa-external-link' not in str(div_content):
            #    #if 'qbase64' not in str(div_content):
            #    print '2'
            #    return None
            #else:
            #    a_text = div_content.find("a")
            #    print a_text['href']

        count = count + 1
        print '-----------'

if __name__ == '__main__':
    #aizhan('www.bstaint.net')
    #oshadan('104.28.31.107')
    fofa('104.28.31.107')
