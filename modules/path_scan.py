#coding=utf-8
'''
Demo modules for ass_hole_hunter
Reprouct from mst
'''
#from libs.functions import *
from libs.functions import *
#import title_banner_hunter


class hunter_plugin:
    '''path scan plugin '''
    infos = {
        'plugin_name':'main_scan module',
        'author':'demon',
        'update':'2015/10/16',
        'site':'http://www.dawner.info',
        }
    opts  = {
        'ping_type':'ping or read',
        'url':'192.168.1.254:23 or site_name',
        }
    def __init__(self,url):
        self.url = url
    def exploit(self):

        #hunter = title_banner_hunter.hunter_plugin(ip,port)
        #hunter.exploit()






















