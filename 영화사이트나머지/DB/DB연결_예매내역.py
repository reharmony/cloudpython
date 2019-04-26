'''
Created on 2019. 4. 10.

@author: user
'''
import pymysql
from 영화사이트화면구성.예매화면2 import *
def reserve_table(reserve_info):
    print(reserve_info)

def db_process_insert(title, time, people, seat_list, seat_total, selectday):
    
    print(title, time, people, seat_total)
    # 1. db인증 -> 연결
    con = pymysql.connect(host ='13.209.92.229', user='root',password='1234', db = 'cloud')
    print("1. db인증 -> 연결 성공...")
    print(con)
    
    # 2. 연결정보 -> 통로
    cur = con.cursor()
    print()
    print("2. 연결정보 -> 통로 만들기 성공...")
    
    # 3. sql문 만들어서 -> 전송
    sql = "insert into reserve (movie_code, time, people, seat) values ('" + title + "', '" + time + "', '" + people + "', '" + seat_total +  "')"
    cur.execute(sql)
    for seat in seat_list:
        print(seat)
#         sql = "update seat set seat_check = 1 where moviecode ='" + title + "' and seat_num ='" + seat + "' and showtime = '" + time + "'"
        sql = "insert into seat values ('" + selectday + "', '" + title + "', '" + time + "', '" + seat +  "')"
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
    
#     
#     print(title, time, people, seat_total)
#     # 1. db인증 -> 연결
#     con = pymysql.connect(host ='localhost', user='root',password='1234', db = 'cloud')
#     print("1. db인증 -> 연결 성공...")
#     print(con)
#     
#     # 2. 연결정보 -> 통로
#     cur = con.cursor()
#     print()
#     print("2. 연결정보 -> 통로 만들기 성공...")
#     
#     # 3. sql문 만들어서 -> 전송
#     sql = "update seat set seat_check = 1 where seat_num ='" + seat_total + "'"
#     cur.execute(sql)    
#     con.commit()
#     
#     
#     print()
#     print("3. sql문 만들어서 -> 전송 성공...")  
#     
#     
#     # 4. db연결해제
#     con.close()
#     print()
#     print("4. db 연결해제 성공...")
#     print("===============================")   
#     print()
#     
#     
    
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
#         print("----------------------------")
#         print("moviecode")
#         print("----------------------------")
#         print(searching)
    
#     print(searching)
#     print(searching[0][0])
#     print(searching[0][1])
#     print(searching[1][0])
#     for x in searching:
#         print(x)    
#     print("\n----------------------------")
    con.commit()
#     return box_list

    # 4. db연결해제
    con.close()
    print()
    print("4. db 연결해제 성공...")
    print("===============================")   
    print()
    
    return searching
    
    
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
#         print("----------------------------")
#         print("moviecode")
#         print("----------------------------")
#         print(searching)
    
    print(searching[0][0])    
#     print(searching[1][0])
#     for x in searching:
#         print(x)    
#     print("\n----------------------------")
    con.commit()
    return searching[0][0]

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
    sql = "select * from movietest"
    n = cur.execute(sql)
    print()
    print("3. sql문 만들어서 -> 전송 성공...")
    result=[]
    
    while True:
        record = cur.fetchone()
        if record == None:
            break
        else:
            print(record)
            result.append(record)
            
#     print(result)
#   
#     print("----------------------------")
#     print("id\ttitle\tcontent\tdirector")
#     print("----------------------------")
#     for x in result:
#         for y in range(len(x)-1):
#             print(x[y], end="\t")
#         print(x[len(x)-1], end="\n")    
#     print("\n----------------------------")
    return result
    con.commit()
    
    # 4. db연결해제
    con.close()
    print()
    print("4. db 연결해제 성공...")
    print("===============================")   
    print()

       
def db_process_update(id, title, content, director, img):
    
    # 1. db인증 -> 연결
    con = pymysql.connect(host ='localhost', user='root',password='1234', db = 'cloud')
    print("1. db인증 -> 연결 성공...")
    print(con)
    
    # 2. 연결정보 -> 통로
    cur = con.cursor()
    print()
    print("2. 연결정보 -> 통로 만들기 성공...")
    
    # 3. sql문 만들어서 -> 전송
    sql = "update movietest set title ='" + title + "', content ='"+ content +"', director='" + director + "', img='" + img + "' where id='" + id + "'"
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
    sql = "delete from movietest where id ='" + id + "'"
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
        print("##### 영화 정보 관리 프로그램 #####")
        select = input("1.입력  2.검색 3.수정 4.삭제 5.전체검색 0.종료 >> ")
          
        if select == '1':  
            print("### 영화 정보를 입력해주세요 ###")
            print("----------------------------")            
            print("----------------------------")        
#             db_process_insert()
        
        elif select == '2':  
            print("### 예매된 좌석을 검색합니다. ###")
            print("----------------------------")
#             selectday = input("날짜입력(ex.20190101)>> ")   
            print("----------------------------")        
            db_process_select()
        
        elif select == '3':  
            print("### 수정할  ID를 입력해주세요 ###")
            print("----------------------------")
            id = input("코드 입력>> ")
            title = input("수정할 제목 입력>> ")
            content = input("수정할 줄거리 입력>> ")
            director = input("수정할 감독 입력>> ")
            director = input("수정할 이미지 주소 입력>> ")
            print("----------------------------")        
            db_process_update(id, title, content, director, img)
        
        elif select == '4':  
            print("### 삭제할 영화코드를 입력해주세요 ###")
            print("----------------------------")
            id = input("코드입력>> ")   
            print("----------------------------")        
            db_process_delete(id)        
                
        elif select == '5':  
            print("### 전체 영화 목록을 불러옵니다 ###")
            print("----------------------------")        
            db_process_selectall()        
        
        elif select == '0':  
            print("### 영화 정보 관리 프로그램을 종료합니다. ###")
            break
        
        else :
            print("잘못된 번호입니다. 다시 입력해주세요.")
            print("----------------------------")        
                 
        
      
    

        
    
    
    
    
    
    
