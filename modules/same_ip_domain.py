#!/usr/bin/env python
#coding=utf-8

from libs.functions import *
#import httplib
#import urllib
#import urllib2
#from bs4 import BeautifulSoup
#import shodan
#import sys
#import os
#import re


#sys.path.append('dbs/')
#from config import global_config


#input_url=raw_input("please input url:")
#option = raw_input("please choose the source:")
#组合排列过滤？

class hunter_plugin:
    infos = {
        'plugin_name':'Title_banner_hunter',
        'author':'demon',
        'update':'2015/04/14',
        'site':'http://www.dawner.info',
        }
    opts  = {
        'input_url':'www.baidu.com or 192.168.0.1',
        }
    def __init__(self,url,api):
        #self.ip = ip
        #self.port = port
        self.url = url
        self.api = api

    def exploit(self):
        config = global_config()
        result_path = config.infos['result_path']
        if not os.path.exists(global_config.infos['result_path']):
            os.mkdir(global_config.infos['result_path'])

        #print result_path
        if ':' in self.url:
            host = self.url.split(':')[0]
        else:
            host = self.url.split('/')[0]
        
        
        if self.api == 'fofa':
            self.fofa(host)
        elif self.api == 'chinaz':
            self.chinaz(host)
        elif self.api == 'oshadan':
            self.oshadan(host)
        elif self.api == 'aizhan':
            self.aizhan(host)
        #elif self.api == 'bgp_he':
        #   self.bgp_he(host)
        else:
            return None

    def chinaz(self,input_url):
        r = open(global_config.infos['result_path']+'chinaz.txt','w+')
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
                            r.writelines(str+'\n')
        r.close()


    def aizhan(self,input_url):

       #if not os.path.exists(global_config.infos['result_path']):
       #     os.mkdir(global_config.infos['result_path'])

        r = open(global_config.infos['result_path']+'aizhan.txt','w+') 
        aizhan_url = 'http://dns.aizhan.com/?q='+input_url
        resp = urllib2.urlopen(aizhan_url).read()
        match = re.search(r'GetDatas.*;',resp)
        data = match.group(0)
        data =  eval('['+data[9:-2]+']')
        #for item in data:
        ip = data[1]
        ajaxkey = data[-1]
        page = 1 
        while(1):
            dic_url = 'http://dns.aizhan.com/index.php?r=index/domains&ip='+ip+'&page='+str(page)+'&q=www.bstaint.net&ajaxkey='+ajaxkey
            try:
                dic_resp = urllib2.urlopen(dic_url).read()
                if dic_resp != "":
                    dic_resp = eval(dic_resp)
                else:
                    return None
                #dic_resp = eval(urllib2.urlopen(dic_url).read())
                #print dic_resp
                #print dic_resp.has_key('domains')
                for value in dic_resp['domains']:
                    print value
                    r.writelines(value+'\n')
            except Exception,e:
                print e
                return None
            page = page + 1
        #print ip,ajaxkey

        #print resp
        #soup = BeautifulSoup(''.join(resp))
        #print type(soup)
        
        #gg01 = soup.find("div", attrs={"class": "gg01"})
        #domains = soup.find_all("input", attrs={"id": "domain"})
        #els = gg01.find_all('a')
        #els=soup.find('div',class_="gg01")
        #els=els.find_all('a')
        
        #for item in domains:
        #    print item['value'].strip()
            #r.writelines(item.text.strip()+'\n')
        r.close()


    def oshadan(self,input_url):
        #log_record("test","e")
        r = open(global_config.infos['result_path']+'oshadan.txt','w+')
        count = 1
        while(1):
            oshadan_url = "https://www.oshadan.com/search?c="+input_url+"&p="+str(count)
            resp = urllib2.urlopen(oshadan_url).read()
            if "请登录" in resp:
                break
            soup = BeautifulSoup(''.join(resp))
            result_info_div = soup.find("div", attrs={"id": "result_info_div"})
            title = result_info_div.find_all("div", attrs={"class": "title"})
            if len(title) == 0:
                return None
            #print len(title)
            #print type(title)
            for t in title:
                try:
                    a = t.find("a")
                    host = a['href'].split('//')[1]
                    print host
                    r.writelines(host+'\n')
                except Exception,e:
                    print e
                    continue
            count = count + 1
            #print "-------------"
        r.close()

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

    #Orz.....bgp need javascript encode post
    #def bgp_he(self,input_url):
    #    #r = open(global_config.infos['result_path']+'bgp_he.)txt','w+')
    #    bgp_he_dns = "http://bgp.he.net/dns/"+input_url+"#_dns"
    #    #print bgp_he_dns
    #    #resp = urllib2.urlopen(bgp_he_url).read()
    #    #req = urllib2.Request(bgp_he_dns)
    #    
    #    cookielib.LWPCookieJar()
    #    
    #    #proxy = urllib2.ProxyHandler({'http':'127.0.0.1:8080'})
    #    
    #    #opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj),proxy)
    #    cookieHandle = urllib2.HTTPCookieProcessor(cj)
    #    opener = urllib2.build_opener(cookieHandle)
    #    opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux i686; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.2.0'),('referer','http://bgp.he.net')]
    #    #req.add_header('User-Agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')
    #    #req.add_header('referer','http://bgp.he.net')
    #    #resp= urllib2.urlopen(req).read()
    #    print bgp_he_dns
    #    #urllib2.install_opener(opener)
    #    req = urllib2.Request(bgp_he_dns)
    #    #resp = urllib2.urlopen(req).read()
    #    resp = opener.open(req).read()
    #    #resp = opener.open(bgp_he_dns).read()
    #    print resp

    #    soup = BeautifulSoup(''.join(resp))
    #    #dnsdata_info_div = soup.find_all("div", attrs={"class": "dnsdata"})[3]
    #    dnsdata_info_divs = soup.find_all("div", attrs={"class": "dnsdata"})
    #    print len(dnsdata_info_divs)
    #    for dnsdata_info_div in dnsdata_info_divs:
    #        print dnsdata_info_div
    #        ip_as = dnsdata_info_div.find_all("a")
    #        print "####"
    #        #ips= []
    #        for ip_a in ip_as:
    #            ip = ip_a.text
    #            #ips.append(ip)
    #            if re.compile(r'\d+\.\d+\.\d+\.\d+',ip):
    #                print ip
    #                pass
    #            else:
    #                print "[x]No ip address."
    #                continue
    #            bgp_he_url = "http://bgp.he.net/ip/"+ip+"#_dns"
    #            #print bgp_he_url
    #            
    #            r_req = urllib2.Request(bgp_he_url)
    #            r_req.add_header('User-Agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')
    #            r_req.add_header('referer','http://bgp.he.net')
    #            r_resp= urllib2.urlopen(r_req).read()
    #            print '------'
    #            r_soup = BeautifulSoup(''.join(r_resp))
    #            result_info_div = r_soup.find("div", attrs={"id": "dns"})
    #            a_text = result_info_div.find_all("a")
    #            r = open(global_config.infos['result_path']+'bgp_he_'+ip+'.txt','w+')
    #            for item in a_text:
    #                print item.text
    #                r.writelines(item.text+'\n')
    #            r.close()


    def fofa(self,input_url):
        r = open(global_config.infos['result_path']+'fofa.txt','w+')
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
                r.writelines(a_text['href']+'\n')
            count = count + 1

        r.close()

if __name__ == '__main__':
    print "test"
    #log_record("test","error")
    #aizhan('www.bstaint.net')
    #oshadan('104.28.31.107')
    #bgp_he('104.28.31.107')
    #fofa('104.28.31.107')
