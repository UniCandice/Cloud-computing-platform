# -*- coding: utf-8 -*-
"""
Created on Sun Jul 05 20:45:43 2015

@author: ssheng
"""

import os
import os.path

path={}
tecplot={}
mysql={}
pbs={}

#filepath=os.path.realpath(__file__)
#prepath,_=os.path.split(filepath)
prepath=r'/data2/Cloud/'
path['upload']=r'/data2/Cloud/'
path['current']=prepath
path['resource']=os.path.join(prepath,'Resource')
path['data']=os.path.join(path['resource'],'database')
path['solver']=os.path.join(path['resource'],'solver')

tecplot['version']=r"#!MC 1310"
tecplot['path']=r"/opt/APP/tecplotchorusde2013r1/tecplot360/bin/tec360"

pbs['qsub']='/usr/local/bin/qsub'
pbs['qstat']='/usr/local/bin/qstat'
pbs['qdel']='/usr/local/bin/qdel'

mysql['host']="localhost"
mysql['port']=3306
mysql['user']="root"
mysql['password']=""
mysql['dbname']="mydata"
mysql['dbname1']="cfd_test"


if __name__=="__main__":
    print "mysql:"
    print mysql
    print "tecplot:"
    print tecplot
    print "path:"
    print path
