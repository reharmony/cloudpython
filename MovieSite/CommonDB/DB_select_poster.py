'''
Created on 2019. 4. 10.

@author: user
'''
import pymysql
from Reserve.Reserve_UI import *

# 선택한 영화의 포스터 파일 이름 받아오기    
def db_process_select_poster(title):
    
    # 1. db인증 -> 연결
    con = pymysql.connect(host ='13.209.92.229', user='root',password='1234', db = 'cloud')
    print("1. db인증 -> 연결 성공...")
    print(con)
    
    # 2. 연결정보 -> 통로
    cur = con.cursor()
    print()
    print("2. 연결정보 -> 통로 만들기 성공...")
    
    # 3. sql문 만들어서 -> 전송
    sql = "select poster from movieinfo where title = '" + title + "'"    
    print()
    print("3. sql문 만들어서 -> 전송 성공...")
    cur.execute(sql)
    searching = cur.fetchall() # 레코드 여러개 조회시 fetchall -> 반복문사용
    print(searching[0][0])    
    con.commit()
    return searching[0][0]

    # 4. db연결해제
    con.close()
    print()
    print("4. db 연결해제 성공...")
    print("===============================")   
    print()


if __name__ == '__main__':
   
    while True :
        print("##### 영화 정보 관리 프로그램 #####")
        select = input("1.포스터 파일의 이름 검색 0.종료 >> ")
          
        if select == '1':  
            print("### 선택된 영화의 포스터 파일명을 검색합니다. ###")
            print("----------------------------")               
            title = input("영화제목 입력(한글)>> ")               
            print("----------------------------")        
            db_process_select_poster(title)
    
        elif select == '0':  
            print("### 영화 정보 관리 프로그램을 종료합니다. ###")
            break
        
        else :
            print("잘못된 번호입니다. 다시 입력해주세요.")
            print("----------------------------")        
                 
        
      
    

        
    
    
    
    
    
    
