#!/usr/bin/env python
#coding=utf-8

import sys

#from what_web import  hunter_plugin
sys.path.append('modules/')
from what_web import  hunter_plugin
import sqlite3
from libs.Threads import ThreadPool
from libs.functions import *

reload(sys)
sys.setdefaultencoding('utf-8')

#cx = sqlite3.connect("../result/result.db")
#cu = cx.cursor()
#cu.execute("DROP TABLE if exists result")
#cu.execute("CREATE TABLE result (id INTEGER primary key AUTOINCREMENT,url VARCHAR(255),status VARCHAR(50), banner VARCHAR(255), cms_type VARCHAR(255), vuln_path VARCHAR(255));")

url = '192.168.1.118:80'
status = 'y'
banner = 'ÂÛÌ³ -  Powered by Discuz!'.decode('utf-8', 'ignore')
cms_type = 'discuz'
vuln_path = ''

#insert = "INSERT INTO result (url ,status ,banner,cms_type,vuln_path) VALUES ('"+url +"','"+status+"','"+banner + "','"+cms_type+"','"+vuln_path +"')"

#cu.execute(insert)
#cx.commit()
#cu.execute("select * from result")
#print str(cu.fetchall())

#attack = hunter_plugin(url,'http')
#print '???'
#attack.exploit()
if __name__ == "__main__":
    tp = ThreadPool(5)
    for line in open('url.txt').readlines():
        hunter = hunter_plugin(line.strip(),'http')
        tp.add_job(hunter.exploit)
    tp.start()
    try:
        tp.wait_for_complete()
        results = tp.get_result()
        print results
    except KeyboardInterrupt:
        tp.stop()



