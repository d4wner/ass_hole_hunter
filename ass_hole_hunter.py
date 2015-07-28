#!/usr/bin/env python
#coding=utf-8
import sys
from libs.Threads import ThreadPool
from libs.color import *
from libs.functions import *


sys.path.append('modules/')
sys.path.append('libs/')
sys.path.append('dbs/')

#from title_banner_hunter import  hunter_plugin
from same_ip_domain import hunter_plugin
import title_banner_hunter


#from main_func import  hunter_plugin

#if __name__ == '__main__':
    #hunter = hunter_plugin(url="192.168.10.103")
    #hunter.exploit()
    #hunter = hunter_plugin()


def title_banner_get():
    from title_banner_hunter import  hunter_plugin
    tp = ThreadPool(5)
    for line in open('url.txt').readlines():
        hunter = hunter_plugin(line)
        tp.add_job(hunter.exploit)
    tp.start()
    try:
        tp.wait_for_complete()
    except KeyboardInterrupt:
        tp.stop()

def same_ip_domain():
    from same_ip_domain import hunter_plugin
    same_ip_query = hunter_plugin('www.bstaint.net','bgp_he')
    same_ip_query.exploit()

if __name__ == '__main__': 
    #title_banner_get()
    same_ip_domain()

    #hunter = hunter_plugin('192.168.10.103:23')
    #hunter.exploit()
    #print hunter.infos

