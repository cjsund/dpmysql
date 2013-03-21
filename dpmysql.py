#!/bin/python
#
#
import os
class dpmysql:
#        user = "root"
#        password = ""
#        address = "127.0.0.1"
#        port = "3306"
#        database = ""
#        backupdir = "/opt/backup/"
#        backupfile = ""
#        charset = "utf-8"
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

#b = dpmysql('root','root','127.0.0.1','3306','test','/opt','mysql.sql','utf8')
#b.backup()
#os.system("ls")
#print "a"
