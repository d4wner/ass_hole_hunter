#!/usr/bin/env python
#coding=utf-8

import sys
import sqlite3

#from what_web import  hunter_plugin
sys.path.append('modules/')
#from what_web import  hunter_plugin
import sqlite3
from libs.Threads import ThreadPool
from libs.functions import *
from modules.path_scan import hunter_plugin
reload(sys)
sys.setdefaultencoding('utf-8')

#cx = sqlite3.connect("../result/result.db")
#cu = cx.cursor()
#cu.execute("DROP TABLE if exists result")
#cu.execute("CREATE TABLE result (id INTEGER primary key AUTOINCREMENT,url VARCHAR(255),status VARCHAR(50), banner VARCHAR(255), cms_type VARCHAR(255), vuln_path VARCHAR(255));")

#url = '192.168.10.103:88/bbs'
#status = 'y'
#banner = 'ÂÛÌ³ -  Powered by Discuz!'.decode('utf-8', 'ignore')
#cms_type = 'discuz'
#vuln_path = ''

#insert = "INSERT INTO result (url ,status ,banner,cms_type,vuln_path) VALUES ('"+url +"','"+status+"','"+banner + "','"+cms_type+"','"+vuln_path +"')"

#cu.execute(insert)
#cx.commit()
#cu.execute("select * from result")
#print str(cu.fetchall())

#===============
#attack = hunter_plugin("www.baidu.com","dic")

#print '???'
#attack.exploit()
cx = sqlite3.connect("dbs/ass.db")
cu = cx.cursor()
cu.execute("select * from vulns")
#print "Result:\n"+ str(cu.fetchall())
contents = cu.fetchall()
for row in contents:
    print row[1]+" | "+row[2]+" | "+row[3]+"\n"


