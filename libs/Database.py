import sqlite3
import os
from glob import glob

#def searchFromDB(keyWord, DBFilePath=r'dbs/MultiProxiesDb.db'):
def search_name(keyWord, dbpath):
    db = sqlite3.connect(dbpath)
    cu = db.cursor()
    cu.execute("select name from  where name like '%" + keyWord + "%'")
    return cu.fetchall()

#def showModulesDict(ModuleType, dbpath):
#    db = sqlite3.connect(dbpath)
#    cu = db.cursor()
#    OutDict = ''
#    ReturnLst = []
#    if ModuleType.lower() in ['auxiliary', 'exploit', '']:
#        cu.execute("select * from ModulesTable where ModuleType like '%" + ModuleType + "%'")
#        for lst in cu.fetchall():
#            ReturnLst.append(lst)
#    return ReturnLst


def return_single_info(tablename,itemname, dbpath):
    db = sqlite3.connect(dbpath)
    cu = db.cursor()
    try:
        #cu.execute("select Module, ModuleName, ModulePath from ModulesTable where id=:id",{"id":int(modulename)})
        cu.execute('select * from '+tablename+'where name='+itemname)
    #except ValueError:
    #    cu.execute("select Module, ModuleName, ModulePath from ModulesTable where Module like:modulename",{"modulename":modulename})

    out = cu.fetchone()
    if out:
        return out

#def listmodules(basepath, modules):
#    import re
#    files = os.listdir(basepath)
#    if ("__init__.py" in files) and not ("private" in files):
#        for path in files:
#            currentpath = os.path.join(basepath, path)
#            filename = os.path.basename(currentpath)
#            if os.path.isfile(currentpath):
#                if not re.match("(__init__\.py[c]?)|([\s\S]+?\.pyc)", filename):
#                    modulepath, ext = os.path.splitext(os.path.relpath(currentpath))
#                    filedir, filename = os.path.split(modulepath)
#                    filepath = modulepath + ext
#                    modulename = modulepath.replace("\\", ".")
#                    modules[filename] = dict()
#                    modules[filename]["filepath"] = filepath
#                    modules[filename]["modulename"] = modulename
#            else:
#                listmodules(currentpath, modules)
#
#def returnAllModules():
#    modules = dict()
#    AllModules = dict()
#    for type in os.listdir(basepath):
#        currentpath = os.path.join(basepath, type)
#        if os.path.isdir(currentpath):
#            AllModules[type] = dict()
#            listmodules(currentpath, modules)
#            AllModules[type] = modules.copy()
#            modules.clear()
#    return AllModules

def update_db():
    
    ''' update CMS database '''
    cms_path = r"dbs/cms/"
    cms_db = sqlite3.connect('dbs/cms.db')

    cms_table_drop = "DROP TABLE IF EXISTS CMS"
    cms_table_create = "create table " \
               "if not exists CMS " \
               "(id integer primary key,name varchar(50) UNIQUE, type varchar(50) UNIQUE)"
    cms_db.execute(cms_table_drop)
    cms_db.execute(cms_table_create)
    cms = dict()
    for cms_name_all in glob(cms_path+'*.txt'):
    #    currentpath = os.path.join(cms_db_path, cms_name)
        cms_name_sig = cms_name_all.split('.')[0]
        cms_name_pre = cms_name_sig.split('_')[0]
        cms[cms_name_pre] = cms_name_sig.split('_')[1]
    
    for cms_name in cms.keys()
        #for module in AllModules[type]:
#        print Module, ModulesType[Module]
    cms_table_insert = 'insert into CMS(name,type) ' \
                        'values("%s","%s")' % (cms_name,cms[cms_name])
    cms_db.execute(cms_table_insert)
    cms_db.commit()

    ''' update EXPLOIT database '''
    exploit_path = r"dbs/exploit/"
    exploit_db = sqlite3.connect('dbs/exploit.db')

    exploit_table_drop = "DROP TABLE IF EXISTS EXPLOIT"
    exploit_table_create = "create table " \
               "if not exists EXPLOIT " \
               "(id integer primary key,name varchar(50) UNIQUE, type varchar(50) UNIQUE,source varchar(200) NULL)"
    exploit_db.execute(exploit_table_drop)
    exploit_db.execute(exploit_table_create)
    exploit = dict()
    for exploit_name_all in glob(exploit_path+'*.py'):
    #    currentpath = os.path.join(cms_db_path, cms_name)
        exploit_name_sig = exploit_name_all.split('.')[0]
        module = __import__(exploit_name_sig)
        getattr(module,hunter_exploit)
        
        exploit_name_pre = exploit_name_sig.split('_')[0]
        #exploit[exploit_name_pre] = exploit_name_sig.split('_')[1]
        exploit[exploit_name_pre] = [hunter_exploit.infos['vuln_type'],hunter_exploit.infos['vuln_source']]

    for exploit_name in exploit.keys()
        exploit_table_insert = 'insert into EXPLOIT(name,type,source) ' \
                        'values("%s","%s","%s")' % (exploit_name,exploit[exploit_name][0],exploit[exploit_name][1])
        exploit_db.execute(exploit_table_insert)
        exploit_db.commit()


def report_db_create(tablename,itemname):
    report_db_path = 'dbs/report/'+itemname+'.db'
    os.system('touch '+ report_db_path)
    report_db = sqlite3.connect(report_db_path)
    report_table_create = "create table "+itemname \
               "(id integer primary key,url varchar(50) UNIQUE, live varchar(50) NULL,banner varchar(200) NULL,cms_type varchar(100) NULL,exploit_name varchar(200) NULL)"
    report_db.execute(report_table_create)
    report_db.commit()
    

def report_db_insert(itemname):
    report_db_path = 'dbs/report/'+itemname+'.db'
    report_db = sqlite3.connect(report_db_path)
    report_table_insert = "insert into "+itemname+ "(url,live,banner,cms_type,exploit_name) values ('%s',NULL,NULL,NULL,NULL)" % itemname
    report_db.execute(report_table_insert)
    report_db.commit()
    
def report_db_update(itemname,up_item,up_item_value,url):
    report_db_path = 'dbs/report/'+itemname+'.db'
    report_db = sqlite3.connect(report_db_path)
    report_table_insert = "update "+itemname+ "set "+up_item+"= '"+up_item_value+"' where url = '"+url+"'"
    report_db.execute(report_table_insert)
    report_db.commit()




#def returnAllModuleLst(AllModules):
#    AllModulesLst = []
#    for type in AllModules:
#        for module in AllModules[type]:
#            AllModulesLst.append(module)
#    return AllModulesLst
#
#def returnDatabaseModuleLst(db=r'db/MultiProxiesDb.db'):
#    db = sqlite3.connect(db)
#
#    cu = db.cursor()
#    cu.execute("select Module from ModulesTable")
#    DataBaseModulesLst = []
#    for module in cu.fetchall():
#        DataBaseModulesLst.append(module[0])
#    return DataBaseModulesLst
#
#AllModules = returnAllModules()
#AllModulesLst = returnAllModuleLst(AllModules)
#DataBaseModulesLst = returnDatabaseModuleLst()
