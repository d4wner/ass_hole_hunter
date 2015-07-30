#!/usr/bin/env python
#coding=utf-8

import sys
import sqlite3

sys.path.append('../dbs/')
from config import global_config

result_db_path = '../'+global_config.infos['result_path']+"/result.db"
cx = sqlite3.connect(result_db_path)
cu = cx.cursor()
cu.execute("select * from result")
print str(cu.fetchall())
