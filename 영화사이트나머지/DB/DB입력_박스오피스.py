#-*- coding:utf-8 -*-

'''
Created on 2019. 4. 10.

@author: user
'''
import pymysql
from 최종_통합 import totalinfo  

def db_process_insert(selectday, rank, moviecode):
    
    # 1. db인증 -> 연결
    con = pymysql.connect(host ='localhost', user='root',password='1234', db = 'cloud')
    print("1. db인증 -> 연결 성공...")
    print(con)
    
    # 2. 연결정보 -> 통로
    cur = con.cursor()
    print()
    print("2. 연결정보 -> 통로 만들기 성공...")
    
    # 3. sql문 만들어서 -> 전송
    sql = "insert into boxoffice values ('" + selectday + "', '"  + rank + "','"+ moviecode + "')"
    cur.execute(sql)
    print()
    print("3. sql문 만들어서 -> 전송 성공...")
    
    con.commit()
    
    # 4. db연결해제
    con.close()
    print()
    print("4. db 연결해제 성공...")
    print("===============================")   
    print()
    
    
def db_process_select(id):
    
    # 1. db인증 -> 연결
    con = pymysql.connect(host ='localhost', user='root',password='1234', db = 'cloud')
    print("1. db인증 -> 연결 성공...")
    print(con)
    
    # 2. 연결정보 -> 통로
    cur = con.cursor()
    print()
    print("2. 연결정보 -> 통로 만들기 성공...")
    
    # 3. sql문 만들어서 -> 전송
    sql = "select * from boxoffice where id = '" + id + "'"
    cur.execute(sql)
    print()
    print("3. sql문 만들어서 -> 전송 성공...")
    searching = cur.fetchone() # 레코드 여러개 조회시 fetchall -> 반복문사용
    print("----------------------------")
    print("id\tpw\tname\ttel")
    print("----------------------------")
#     for x in searching:
#         id = searching[0]
#         pw = searching[1]
#         name = searching[2]
#         tel = searching[3]
#     print("%s\t%s\t%s\t%s" % (id,pw,name,tel))
    for x in searching:
        print(x, end="\t")    
    print("\n----------------------------")
    return searching
    con.commit()
    
    # 4. db연결해제
    con.close()
    print()
    print("4. db 연결해제 성공...")
    print("===============================")   
    print()
    
def db_process_selectall():
    
    # 1. db인증 -> 연결
    con = pymysql.connect(host ='localhost', user='root',password='1234', db = 'cloud')
    print("1. db인증 -> 연결 성공...")
    print(con)
    
    # 2. 연결정보 -> 통로
    cur = con.cursor()
    print()
    print("2. 연결정보 -> 통로 만들기 성공...")
    
    # 3. sql문 만들어서 -> 전송
    sql = "select * from boxoffice"
    cur.execute(sql)
    print()
    print("3. sql문 만들어서 -> 전송 성공...")
    searching = None
    searching = cur.fetchall() # 레코드 여러개 조회시 fetchall -> 반복문사용
    print("----------------------------")
    print("id\tpw\tname\ttel")
    print("----------------------------")
    return 
    for x in searching:
        print(x, end="\t")    
    
       

       
    # 4. db연결해제
    con.close()
    print()
    print("4. db 연결해제 성공...")
    print("===============================")   
    print()
    
def db_process_update(id, pw, name, tel):
    
    # 1. db인증 -> 연결
    con = pymysql.connect(host ='localhost', user='root',password='1234', db = 'cloud')
    print("1. db인증 -> 연결 성공...")
    print(con)
    
    # 2. 연결정보 -> 통로
    cur = con.cursor()
    print()
    print("2. 연결정보 -> 통로 만들기 성공...")
    
    # 3. sql문 만들어서 -> 전송
    sql = "update boxoffice set pw ='" + pw + "', name ='"+ name +"', tel='" + tel + "' where id='" + id + "'"
    print(sql)
    cur.execute(sql)
    print()
    print("3. sql문 만들어서 -> 전송 성공...")
    
    con.commit()
    
    # 4. db연결해제
    con.close()
    print()
    print("4. db 연결해제 성공...")    
    print("===============================")
    print()
    
    
def db_process_delete(id):
    
    # 1. db인증 -> 연결
    con = pymysql.connect(host ='localhost', user='root',password='1234', db = 'cloud')
    print("1. db인증 -> 연결 성공...")
    print(con)
    
    # 2. 연결정보 -> 통로
    cur = con.cursor()
    print()
    print("2. 연결정보 -> 통로 만들기 성공...")
    
    # 3. sql문 만들어서 -> 전송
    sql = "delete from boxoffice where id ='" + id + "'"
    cur.execute(sql)
    print()
    print("3. sql문 만들어서 -> 전송 성공...")
    
    con.commit()
    
    # 4. db연결해제
    con.close()
    print()
    print("4. db 연결해제 성공...")
    print("===============================")    
    print()
    
    
    

if __name__ == '__main__':
   
    while True :
        print("##### DB 관리 프로그램 #####")
        select = input("1.가입  2.검색 3.수정 4.삭제 0.종료 >> ")
          
        if select == '1':  
            print("### 박스오피스 정보를 DB에 전송합니다. ###")
            print("----------------------------")
           
            all = totalinfo()
            for i in range(0,10):
                one = all[i]
                print(one) 
                selectday = one[0]
                rank = one[1]               
                moviecode = one[5]
           
                db_process_insert(selectday, rank, moviecode)
                
            print("----------------------------")        
#             
        
        elif select == '2':  
            print("### 검색할 ID를 입력해주세요 ###")
            print("----------------------------")
            id = input("ID입력>> ")   
            print("----------------------------")        
            db_process_select(id)
        
        elif select == '3':  
            print("### 수정할  ID를 입력해주세요 ###")
            print("----------------------------")
            id = input("ID입력>> ")
            pw = input("수정할 PW입력>> ")
            name = input("수정할 NAME입력>> ")
            tel = input("수정할 TEL입력>> ")
            print("----------------------------")        
            db_process_update(id, pw, name, tel)
        
        elif select == '4':  
            print("### 삭제할 ID를 입력해주세요 ###")
            print("----------------------------")
            id = input("ID입력>> ")   
            print("----------------------------")        
            db_process_delete(id)
        
        elif select == '5':
            print("### 전체 회원 목록을 보여줍니다 ###")
            print("----------------------------")
            db_process_selectall()
    
        elif select == '0':  
            print("### DB프로그램을 종료합니다. ###")
            break
        
        else :
            print("잘못된 번호입니다. 다시 입력해주세요.")
            print("----------------------------")        
                 
        
      
    

        
    
    
    
    
    
    
