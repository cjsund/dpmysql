#!/bin/python
#
#
import os
class dpmysql:
    def __init__(self,u='root',p='',a='127.0.0.1',P='3306',d='terst',D='~/',f='',U='utf-8'):
        self.user = u
        self.password = p
        self.address = a
        self.port = P
        self.database = d
        self.backupdir = D
        self.backupfile = f
        self.charset = U
    def backup(self):
        print("mysqldump -u%s -p%s -h%s -P%s --default-character-set=%s %s > %s/%s" % (self.user,self.password,self.address,self.port,self.charset,self.database,self.backupdir,self.backupfile))
        os.system("mysqldump -u%s -p%s -h%s -P%s --default-character-set=%s %s > %s/%s" % (self.user,self.password,self.address,self.port,self.charset,self.database,self.backupdir,self.backupfile))

