#coding=utf-8
'''
Demo modules for ass_hole_hunter
Reprouct from mst
'''
#from libs.functions import *
from libs.functions import *
#import title_banner_hunter
success_path = []
global success_path

class hunter_plugin:
    '''path scan plugin '''
    infos = {
        'plugin_name':'path_scan module',
        'author':'demon',
        'update':'2015/10/20',
        'site':'http://www.dawner.info',
        }
    opts  = {
        'url':'192.168.1.254:23 or site_name',
        }
    def __init__(self,url,dic,port,path):
        self.dic = dic
        self.url = url
        self.port = port
        self.path = path

    def exploit(self):
        tp = ThreadPool(global_config.infos['thread_num'])
        test_resp = url_Head(self.url,'/sbhacker.html')
        if test_resp.status  != 200:
            for line in open('dbs/dic/'+self.dic+'.txt','r').readlines():
                args = []
                args.append(line.strip())
                try:
                    tp.add_job(self.head_req,args)
                except:
                    pass
                #resp = url_head(url,line.strip())
        else:
            exit(0)
        try:
            tp.start()
            tp.wait_for_complete()
        except KeyboardInterrupt:
            tp.stop()
    def head_req(self,*args):
        #success_path = []
        path = self.path+args[0]
        try:
            #resp = url_post(self.url)
            #print resp.read()
            resp = url_Head(self.url,path,port)
            print resp.status
            if resp.status == 200:
                #return args[0]
                success_path.append(args[0])
            else:
                pass
        except:
            print e
            return success_path

        #hunter = title_banner_hunter.hunter_plugin(ip,port)
        #hunter.exploit()

