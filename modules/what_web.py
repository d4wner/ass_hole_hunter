#coding=utf-8
'''
Demo modules for ass_hole_hunter
Reprouct from mst
'''
#from libs.functions import *
#import modules.*
import hashlib
import json
import sqlite3
import requests
from libs.Threads import ThreadPool
from libs.functions import *


class hunter_plugin:
    '''cms feature detect'''
    infos = {
        'plugin_name':'what_web module',
        'author':'demon',
        'update':'2015/04/22',
        'site':'http://www.dawner.info',
        }
    opts  = {
        'url':'192.168.1.254 or default',
        'protocol':'http or https or other',
        'threads':'10'
        }
    
    
    def __init__(self,url,protocol):
        self.url = url
        self.protocol = protocol


    def exploit(self):
        if self.protocol == 'http' or self.protocol == 'https':
            url = self.protocol+'://'+self.url+'/'
        else:
            return None
        print 'exp_start...'
        print url+'\n'
        self.cmsjsons = self.retcmsjsons('dbs/cms.txt')
        #threadsNum = int(self.opts['threads'])
        ThreadsNum = 10
        '''threads can be set in opts  '''
        #sites = self.options['sites']
        #sitesLst = retSites(sites)
        
        #ArgsLst = self.retArgs(sitesLst, self.cmsjsons)
        ArgsLst = self.retArgs(url, self.cmsjsons)
        #threadsDo(self.whatCMS, threadsNum, ArgsLst)
        tp = ThreadPool(ThreadsNum)
        for Args in ArgsLst:
            #print Args
            tp.add_job(self.whatCMS, Args)
        tp.start()
        try:
            tp.wait_for_complete()
        except KeyboardInterrupt:
            tp.stop()
        print 'exp_stop...'

        #if len(self.result):
        #    logByLine(self.result,'output/%s-whatcms.txt' % currentTime("-"))


    def retArgs(self, url, cmsjsons):
        ArgsLst = []
        #for site in siteslst:
        for cmsname in cmsjsons:
            for record in cmsjsons[cmsname]:
                path = record["path"]
                ArgsLst.append((url, path,))
        return list(set(ArgsLst))


    def retcmsjsons(self, jsonfilepath="db/cms.txt"):
        with open(jsonfilepath) as f:
            cmsjsons = json.loads(f.read())
        f.close()
        return cmsjsons

    def getcmsnamefromresp(self, path, resp, cmsjsons):
        for cmsname in cmsjsons:
            for record in cmsjsons[cmsname]:

                if record["path"] == path:

                    if record.has_key("version"):
                        version = record["version"]
                    else:
                        version = " Version missing..."

                    if record.has_key("status_code"):
                        if resp.status_code == record["status_code"]:
                            return (cmsname,version)

                    elif record.has_key("regex"):
                        if re.search(record["regex"], resp.content):
                            print "regex"
                            return (cmsname,version)

                    elif record.has_key("md5"):
                        responsehash = hashlib.md5(resp.content).hexdigest()
                        if str(responsehash) == record["md5"]:
                            return (cmsname,version)
                    else:
                        return None
                    break


    def cms_attack(self, site, cms):
        cx = sqlite3.connect("dbs/ass.db")
        cu = cx.cursor()
        cu.execute("select vuln_path from vulns where vuln_path like '%"+cms+"%'")
        tp = ThreadPool(5)
        #print str(cu.fetchall())
       #线程池
        for paths in cu.fetchall():
            for path in paths:
                print str(path)
                #print str(cu.fetchall())
                print "[+]vuln_path:"+str(path)
                exp_plugin=__import__(path, fromlist=[path])
                hunter_exploit = getattr(exp_plugin,'hunter_exploit')
                #hunter_exploit.exploit(site)
                hunter_exploit = hunter_exploit(site)
                print '-------'
                tp.add_job(hunter_exploit.exploit)
        tp.start()
        try:
            tp.wait_for_complete()
        except:
            tp.stop()

    def whatCMS(self, site, path):
        try:
            checkurl = site + path
            #color.echo("[*] checking %s \r" % path[0:40].ljust(40," "),None, append=True)
            #print checkurl+'-------'
            resp = url_Get(requests, checkurl)
            result = self.getcmsnamefromresp(path, resp, self.cmsjsons)
            if result:
                #if not (site, result[0]) in self.result:
                print site, result[0].split('@')[0], result[1]
                    #color.echo("[+]%s : %s ver: %s \t" % (site, result[0].split('@')[0]), result[1], GREEN)
                print str(result[0].split('@')[0])
                self.cms_attack(site, str(result[0].split('@')[0]))
                    #self.result.append((site, result[0]))
                #self.log.append((site, path, result[0], result[1]))
        except Exception,e:
            print e
            pass


#    def cms_attack(site, cms):
#        cx = sqlite3.connect("result/result.db")
#        cu = cx.cursor()
#        cu.execute("select vuln_path from result where vuln_path like '%"+cms+"%'")
#        tp = ThreadPool(5)
#       #线程池
#        for path in cu.fetchall():
#            print "[+]vuln_path:"+item
#            exp_plugin=__import__(path, fromlist=[path])
#            hunter_exploit = getattr(exp_plugin,'hunter_exploit')
#            #hunter_exploit.exploit(site)
#            tp.add_job(hunter_exploit.exploit(site))
#        tp.start()
#        try:
#            tp.wait_for_complete()
#        except:
#            tp.stop()

