#-*- coding:utf-8 -*-

'''
Created on 2019. 4. 10.

@author: user
'''
import pymysql
from 최종_통합 import totalinfo  

def db_process_insert(moviecode, title, engtitle, openday, people, runningtime, age, genre, director, actor, poster, star):
    
    # 1. db인증 -> 연결
    con = pymysql.connect(host ='localhost', user='root',password='1234', db = 'cloud')
    print("1. db인증 -> 연결 성공...")
    print(con)
    
    # 2. 연결정보 -> 통로
    cur = con.cursor()
    print()
    print("2. 연결정보 -> 통로 만들기 성공...")
    
    # 3. sql문 만들어서 -> 전송
    sql = "insert into movieinfo values ('" + moviecode + "','"+ title + "','" + engtitle + "','" + openday + "','" + people + "','" + runningtime + "','" + age + "', '" + genre + "', '" + director + "', '" + actor + "', '" + poster + "','" + star + "')"
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
    sql = "select * from member where id = '" + id + "'"
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
    sql = "select * from member"
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
    sql = "update member set pw ='" + pw + "', name ='"+ name +"', tel='" + tel + "' where id='" + id + "'"
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
    sql = "delete from member where id ='" + id + "'"
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
            print("### 영화 정보를 DB에 전송합니다. ###")
            print("----------------------------")
           
            all = totalinfo()
            for i in range(0,10):
                one = all[i]
                print(one)                
                title = one[2]
                openday = one[3]
                people = one[4]
                moviecode = one[5]
                engtitle = one[6]
                runningtime = one[7]
                age = one[8]
                genre=""
                genlist=""
                if len(one[9][0]) < 2: 
                    genre = one[9]
                else:
                    for i in range(len(one[9])-1): 
                        genre += one[9][i] + ", "
                    genre += one[9][len(one[9])-1] 
                director=""
                dirlist=""
                if len(one[10][0]) < 2: 
                    director = one[10]
                else:
                    for i in range(len(one[10])-1): 
                        director += one[10][i] + ", "
                    director += one[10][len(one[10])-1] 
                actor=""
                actlist=""
                if len(one[11][0]) < 2: 
                    actor = one[11]
                else:
                    for i in range(len(one[11])-1): 
                        actor += one[11][i] + ", "
                    actor += one[11][len(one[11])-1] 
                poster = one[12]
                star = one[13]
                db_process_insert(moviecode, title, engtitle, openday, people, runningtime, age, genre, director, actor, poster, star)
                
            print("----------------------------")        
#             
        
        elif select == '2':  
            print("### 영화의 코드를 입력해주세요 ###")
            print("----------------------------")
            id = input("코드입력>> ")   
            print("----------------------------")        
            db_process_select(id)
        
        elif select == '3':  
            print("### 정보를 수정할 영화의 코드를 입력해주세요 ###")
            print("----------------------------")
            id = input("코드입력>> ")
            pw = input("수정할 PW입력>> ")
            name = input("수정할 NAME입력>> ")
            tel = input("수정할 TEL입력>> ")
            print("----------------------------")        
            db_process_update(id, pw, name, tel)
        
        elif select == '4':  
            print("### 정보를 삭제할 영화의 코드를 입력해주세요 ###")
            print("----------------------------")
            id = input("코드입력>> ")   
            print("----------------------------")        
            db_process_delete(id)
        
        elif select == '5':
            print("### 전체 영화 목록을 보여줍니다 ###")
            print("----------------------------")
            db_process_selectall()
    
        elif select == '0':  
            print("### DB프로그램을 종료합니다. ###")
            break
        
        else :
            print("잘못된 번호입니다. 다시 입력해주세요.")
            print("----------------------------")        
                 
        
      
    

        
    
    
    
    
    
    
