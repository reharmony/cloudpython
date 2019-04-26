'''
Created on 2019. 4. 10.

@author: user
'''
import pymysql
from Reserve.Reserve_UI import *
def reserve_table(reserve_info):
    print(reserve_info)

# 예약된 좌석번호 검색
def db_process_select_reserve(title, time, yesterday):
    
    # 1. db인증 -> 연결
    con = pymysql.connect(host ='13.209.92.229', user='root',password='1234', db = 'cloud')
    print("1. db인증 -> 연결 성공...")
    print(con)
    
    # 2. 연결정보 -> 통로
    cur = con.cursor()
    print()
    print("2. 연결정보 -> 통로 만들기 성공...")
    
    # 3. sql문 만들어서 -> 전송
    sql = "select seat_num from seat where moviecode ='" + title + "'  and showtime = '" + time + "'" + "and selectday = '" + yesterday + "'"
    print()
    print("3. sql문 만들어서 -> 전송 성공...")
    cur.execute(sql)
    searching = cur.fetchall() # 레코드 여러개 조회시 fetchall -> 반복문사용

    con.commit()

    # 4. db연결해제
    con.close()
    print()
    print("4. db 연결해제 성공...")
    print("===============================")   
    print()
    
    return searching
  
  
if __name__ == '__main__':
   
    while True :
        print("##### 영화 정보 관리 프로그램 #####")
        select = input("1.입력  2.검색 3.수정 4.삭제 5.전체검색 0.종료 >> ")
             
        if select == '1':  
            print("### 예매된 좌석을 검색합니다. ###")
            print("----------------------------")
            selectday = input("상영날짜 입력(ex.20190101)>> ")   
            title = input("영화제목 입력(한글)>> ")   
            time = input("상영시간 입력(ex.09:00)>> ")   
            print("----------------------------")        
            db_process_select_reserve(title, time, selectday)
     
        elif select == '0':  
            print("### 영화 정보 관리 프로그램을 종료합니다. ###")
            break
        
        else :
            print("잘못된 번호입니다. 다시 입력해주세요.")
            print("----------------------------")        
                 
        
      
    

        
    
    
    
    
    
    
