# -*- coding: utf-8 -*-
"""
Created on Fri Jun 05 14:29:22 2015

@author: xiaosheng
"""

import MySQLdb
#import csv,os,os.path
import constant

def call_case():
    db=MySQLdb.connect(constant.mysql['host'],constant.mysql['user'],constant.mysql['password'],constant.mysql['dbname'])
    cursor=db.cursor()

    sql="""select * from cfd_case"""
    
    try:
        cursor.execute(sql)
        results=cursor.fetchall()
        
    except:
        print 'Error: unable to fetch data'
    db.close()
    return results


def call_sts():
    db=MySQLdb.connect(constant.mysql['host'],constant.mysql['user'],constant.mysql['password'],constant.mysql['dbname'])
    cursor=db.cursor()
    
    sql="""select * from cfd_sts"""
    
    try:
        cursor.execute(sql)
        results=cursor.fetchall()
       
    except:
        print 'Error: unable to fetch data'
    db.close()
    return results

def select_case(name):
    db=MySQLdb.connect(constant.mysql['host'],constant.mysql['user'],constant.mysql['password'],constant.mysql['dbname'])
    cursor=db.cursor()
    
    results=[]
    for search in name:
        sql="""select * from cfd_case where name='%s'""" %(search)
        try:
            cursor.execute(sql)
            row=cursor.fetchone()
            
            results.append(row)
        except:
            print 'Error: unable to fetch data'
    
    db.close()
    return results

def select_sts(case_name):
    db=MySQLdb.connect(constant.mysql['host'],constant.mysql['user'],constant.mysql['password'],constant.mysql['dbname'])
    cursor=db.cursor()
    
    search=case_name
    sql="""select * from cfd_sts where case_id='%d'""" %(search)

    try:
        cursor.execute(sql)
        results=cursor.fetchall()
    except:
        print 'Error: unable to fetch data'
    db.close()
    return results

def select_sts19(case_name):
    db=MySQLdb.connect(constant.mysql['host'],constant.mysql['user'],constant.mysql['password'],constant.mysql['dbname'])
    cursor=db.cursor()
    
    search=case_name
    sql="""select * from cfd_sts19 where case_id='%d'""" %(search)

    try:
        cursor.execute(sql)
        results=cursor.fetchall()
    except:
        print 'Error: unable to fetch data'
    db.close()
    return results

if __name__=='__main__':
    testcase=['stq','dun']
    case=select_case(testcase)
    for line in case:
        slist=select_sts(line[0])
        sourcecase=line[1]
        print sourcecase
        for s in slist:
             print s[2]
             print s[62]
           
    
    
