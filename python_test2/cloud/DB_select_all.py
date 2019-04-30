'''
Created on 2019. 4. 30.

@author: user
'''

import pymysql
from cloud.UI_Main import *

# 수강정보 DB에서 모든 자료 출력
def db_process_select_all():
    
    # 1. db인증 -> 연결
    con = pymysql.connect(host ='localhost', user='root',password='1234', db = 'course')
    print("1. db인증 -> 연결 성공...")
    print(con)
    
    # 2. 연결정보 -> 통로
    cur = con.cursor()
    print()
    print("2. 연결정보 -> 통로 만들기 성공...")
    
    # 3. sql문 만들어서 -> 전송
    sql = "select * from course_info" 
    cur.execute(sql) 
    result = cur.fetchall()
    
    con.commit()
   
    print()
    print("3. sql문 만들어서 -> 전송 성공...")  
    
    # 4. db연결해제
    con.close()
    print()
    print("4. db 연결해제 성공...")
    print("===============================")   
    print()
    
    return result