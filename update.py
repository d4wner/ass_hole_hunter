#!/usr/bin/env python
#coding=utf-8

#update database sqlite
#table:cms,vluns

import sqlite3
import sys
import os
import json
#sys.path.append('dbs/exploit/*')

global cu,cx

def GetFileList(dir, fileList):
    newDir = dir 
    #print os.path.splitext(dir)[1]
    if os.path.isfile(dir):
        if os.path.splitext(dir)[1] == ".py~" or os.path.splitext(dir)[1] == ".pyc":
            return None
        fileList.append(dir)
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            #如果需要忽略某些文件夹，使用以下代码
            if s == "demo" or s == '__init__.py' or s== 'pass_big.txt' or s == 'path.txt':
                continue
            newDir=os.path.join(dir,s)
            GetFileList(newDir, fileList)
    return fileList

def vulns(plugins):
    for e in plugins:
        #print e
        exp = os.path.basename(e).split('.')[0]
        exp_type = e.split('/')[-2]
        exp_plugin=__import__("dbs.exploit."+exp_type+'.'+exp, fromlist=[exp])
        #print exp_plugin
        print '---------------------------------------------------'
        hunter_exploit = getattr(exp_plugin,'hunter_exploit')
        vuln_name = hunter_exploit.infos['plugin_name']
        vuln_type = hunter_exploit.infos['vuln_type']
        vuln_source = hunter_exploit.infos['vuln_source']
        vuln_path = "dbs.exploit."+exp_type+'.'+exp
        print vuln_path
        print '---------------------------------------------------'
        insert = "INSERT INTO vulns (vuln_name,vuln_type , vuln_source ,vuln_path) VALUES ('"+vuln_name +"','"+vuln_type+"','"+vuln_source + "','"+vuln_path +"')"
        print insert
        cu.execute(insert)
        cx.commit()
    cu.execute("select * from vulns")
    print "Result:\n"+ str(cu.fetchall())

#def cms():
#    f = file("dbs/cms.txt")
#    s = json.load(f)
#    for key in s.keys():
#        print key.lower()
#    for e in plugins:
#        #print e
#        exp = os.path.basename(e).split('.')[0]
#        exp_type = e.split('/')[-2]
#        exp_plugin=__import__("dbs.cms."+exp_type+'.'+exp, fromlist=[exp])
#        #print exp_plugin
#        print '---------------------------------------------------'
#        hunter_exploit = getattr(exp_plugin,'hunter_exploit')
#        vuln_name = hunter_exploit.infos['plugin_name']
#        vuln_type = hunter_exploit.infos['vuln_type']
#        vuln_source = hunter_exploit.infos['vuln_source']
#        print '---------------------------------------------------'
#        insert = "INSERT INTO vulns (vuln_name,vuln_type , vuln_source) VALUES ('"+vuln_name +"','"+vuln_type+"','"+vuln_source +"')"
#        print insert
#        cu.execute(insert)
#        cx.commit()
#    cu.execute("select * from vulns")
#    print "Result:\n"+ str(cu.fetchall())

if __name__ == '__main__':
    print 'Sql conneting...'
    cx = sqlite3.connect("dbs/ass.db")
    cu = cx.cursor()
    cu.execute("DROP TABLE if exists cms ")
    cu.execute("DROP TABLE if exists vulns ")
    """ create cms and vulns"""
    cu.execute("CREATE TABLE cms (id INTEGER primary key AUTOINCREMENT,cms_name VARCHAR(255),cms_type VARCHAR(50));")
    cu.execute("CREATE TABLE  vulns (id INTEGER primary key AUTOINCREMENT,vuln_name VARCHAR(255),vuln_type VARCHAR(50),vuln_source VARCHAR(255),vuln_path VARCHAR(255));")
    

    """ vluns """
    plugins = GetFileList('./dbs/exploit', [])
    vulns(plugins)

    """ cms """
    #plugins = GetFileList('./dbs/cms', [])
    #cms()
    #cms update by handed defaultly.

    ##print plugins
    #for e in plugins:
    #    #print e
    #    exp = os.path.basename(e).split('.')[0]
    #    exp_type = e.split('/')[-2]
    #    exp_plugin=__import__("dbs.exploit."+exp_type+'.'+exp, fromlist=[exp])
    #    #print exp_plugin
    #    print '---------------------------------------------------'
    #    hunter_exploit = getattr(exp_plugin,'hunter_exploit')
    #    vuln_name = hunter_exploit.infos['plugin_name']
    #    vuln_type = hunter_exploit.infos['vuln_type']
    #    vuln_source = hunter_exploit.infos['vuln_source']
    #    print '---------------------------------------------------'
    #    insert = "INSERT INTO vulns (vuln_name,vuln_type , vuln_source) VALUES ('"+vuln_name +"','"+vuln_type+"','"+vuln_source +"')"
    #    print insert
    #    cu.execute(insert)
    #    cx.commit()
    #cu.execute("select * from vulns")
    #print "Result:\n"+ str(cu.fetchall())


