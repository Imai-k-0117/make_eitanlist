#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 10:34:32 2018

@author:
"""

import csv
import MySQLdb

connection = MySQLdb.connect(db="----",user="root",passwd="------",host='localhost')
cursor=connection.cursor()

count = 0;

#table 作成
sql = 'create table name (id int, content varchar(32), content2 varchar(32), content3 varchar(32))'
cursor.execute(sql)
print('* testテーブルを作成\n')

# テーブル一覧の取得
#sql = 'show tables;'
#cursor.execute(sql)
#print('===== テーブル一覧 =====')
#print(cursor.fetchone())

f = open("------.csv", "r")
reader = csv.reader(f)


#一行目を取得
#header = next(reader)
#print(header) 


for row in reader:
  sql = "INSERT IGNORE INTO name values(%s,%s,%s,%s)"
  count += 1;
  print(count,row[0], row[1], row[2])
  cursor.execute(sql, (count,row[0], row[1], row[2]))
  
f.close()

connection.commit()
cursor.close()
connection.close()