#!/usr/bin/env python
#coding=utf-8
import sys
import sqlite3
import time

from libs.Threads import ThreadPool
from libs.color import *
from libs.functions import *


sys.path.append('modules/')
sys.path.append('libs/')
sys.path.append('dbs/')

#from title_banner_hunter import  hunter_plugin
from same_ip_domain import hunter_plugin
import title_banner_hunter
from config import global_config

reload(sys)
sys.setdefaultencoding('utf-8')

#from main_func import  hunter_plugin

#if __name__ == '__main__':
    #hunter = hunter_plugin(url="192.168.10.103")
    #hunter.exploit()
    #hunter = hunter_plugin()


def what_web():
    from what_web import  hunter_plugin
    result_db_path = global_config.infos['result_path']+"/result.db"
    cx = sqlite3.connect(result_db_path)
    cu = cx.cursor()
    cu.execute("select url,protocol from result")
    tp = ThreadPool(5)
    for item in cu.fetchall():
        #print item[0],item[1]
        url = item[0]
        protocol = item[1]
        cms_attack = hunter_plugin(url,protocol)
        #cms_attack.exploit()
        tp.add_job(cms_attack.exploit)
    tp.start()
    try:
        tp.wait_for_complete()
    except KeyboardInterrupt:
        tp.stop()



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

def crete_tmp_db():
    print 'Creating tmp_result_db...'
    result_db_path = global_config.infos['result_path']+"/result.db"
    cx = sqlite3.connect(result_db_path)
    cu = cx.cursor()
    cu.execute("DROP TABLE if exists result")
    cu.execute("CREATE TABLE result (id INTEGER primary key AUTOINCREMENT,url VARCHAR(255),protocol VARCHAR(50),banner VARCHAR(255),cms_type VARCHAR(255) ,vuln_confirm  VARCHAR(50));")
    time.sleep(1)
    print 'Result_db has been init...'

    #if not os.path.exists(result_db_path):
    #    os.mkdir(result_db_path)

   # cx = sqlite3.connect(result_db_path)





if __name__ == '__main__':
    crete_tmp_db()
    title_banner_get()
    time.sleep(3)
    what_web()
    #same_ip_domain()

    #hunter = hunter_plugin('192.168.10.103:23')
    #hunter.exploit()
    #print hunter.infos

