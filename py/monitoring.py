# -*- coding: utf-8 -*-
"""
Created on Sun Jul 05 20:45:43 2015

@author: ssheng
"""

import os,sys
import os.path
import constant
import subprocess
import optparse
def mon_node():
    monit_path=os.path.join(constant.path['current'],'mon_node.txt')
    f=open(monit_path,'w')
    cmd=r"sh findEmpties.sh"
    proc=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,)
    remainder=proc.communicate()[0]
    f.write(remainder)
    f.close

def mon_job():
    monit_path=os.path.join(constant.path['current'],'mon_job.txt')
    f=open(monit_path,'w')
    cmd=r"sh FindEmpties.sh"
    proc=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,)
    remainder=proc.communicate()[0]
    f.write(remainder)
    f.close

def main(args):

    parser=optparse.OptionParser()
    parser.add_option('-n','--node',dest="nflag",default=False,action="store_true")
    parser.add_option('-j','--job',dest="jflag",default=False,action="store_true")
    option,args=parser.parse_args()
    runflag=False

    if option.nflag:
        mon_node()
        runflag=True
    if option.jflag:
        mon_job()
        runflag=True
if __name__=="__main__":
    main(sys.argv)

