#coding=utf-8
'''
Created on 2014-11-14
 
@author: Neo
'''
import os

def GetFileList(dir, fileList):
    newDir = dir
    #print os.path.splitext(dir)[1]
    if os.path.isfile(dir):
        if os.path.splitext(dir)[1] == ".py~":
            return None
        fileList.append(dir.decode('gbk'))
    elif os.path.isdir(dir):  
        for s in os.listdir(dir):
            #如果需要忽略某些文件夹，使用以下代码
            #if os.path.splitext(s) == "py~":
            #    continue
            newDir=os.path.join(dir,s)
            GetFileList(newDir, fileList)  
    return fileList
 
list = GetFileList('../dbs/exploit', [])
for e in list:
    print e
