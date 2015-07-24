# -*- coding: cp936 -*-
'''
Demo modules for ass_hole_hunter
Reprouct from mst
'''
#from libs.functions import *
import title_banner_hunter


class hunter_plugin:
    '''main_scan'''
    infos = {
        'plugin_name':'main_scan module',
        'author':'demon',
        'update':'2015/04/17',
        'site':'http://www.dawner.info',
        }
    opts  = {
        'ping_type':'ping or read',
        'url':'192.168.1.254:23 or site_name',
        }
    def __init__(self,url):
        self.url = url
    def exploit(self):
        '''start exploit'''
        if ":" in self.url:
            ip = self.url.split(':')[0]
            port = self.url.split(':')[1].strip()
        else:
            ip = self.url.strip()
            port = "80"
        #print "=="+ip+"=="+port+"=="
        hunter = title_banner_hunter.hunter_plugin(ip,port)
        hunter.exploit()






















