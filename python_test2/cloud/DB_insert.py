'''
Created on 2019. 4. 30.

@author: user
'''

import pymysql
from cloud.UI_Main import *

# 수강정보 DB에 입력
def db_process_insert(id, subject, content, price, people):
    
    # 1. db인증 -> 연결
    con = pymysql.connect(host ='localhost', user='root',password='1234', db = 'course')
    print("1. db인증 -> 연결 성공...")
    print(con)
    
    # 2. 연결정보 -> 통로
    cur = con.cursor()
    print()
    print("2. 연결정보 -> 통로 만들기 성공...")
    
    # 3. sql문 만들어서 -> 전송
    sql = "insert into course_info values ('" + id + "', '" + subject + "', '" + content + "', %d, %d)" % (int(price), int(people))
    cur.execute(sql) 
    con.commit()
   
    print()
    print("3. sql문 만들어서 -> 전송 성공...")  
    
    # 4. db연결해제
    con.close()
    print()
    print("4. db 연결해제 성공...")
    print("===============================")   
    print()