'''
Created on 2019. 4. 10.

@author: user
'''
import pymysql

def db_process_insert(id, title, content, director,img):
    
    # 1. db인증 -> 연결
    con = pymysql.connect(host ='localhost', user='root',password='1234', db = 'cloud')
    print("1. db인증 -> 연결 성공...")
    print(con)
    
    # 2. 연결정보 -> 통로
    cur = con.cursor()
    print()
    print("2. 연결정보 -> 통로 만들기 성공...")
    
    # 3. sql문 만들어서 -> 전송
    sql = "insert into movietest values ('" + id + "', '" + title + "', '" + content + "', '"+ director + "', '"+ img + "')"
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
    sql = "select * from movietest where id = '" + id + "'"
    cur.execute(sql)
    print()
    print("3. sql문 만들어서 -> 전송 성공...")
    searching = cur.fetchone() # 레코드 여러개 조회시 fetchall -> 반복문사용
    print("----------------------------")
    print("id\ttitle\tcontent\tdirector")
    print("----------------------------")
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
            id = input("영화 코드>> ")
            title = input("제목 입력>> ")
            content = input("줄거리 입력>> ")
            director = input("감독 입력>> ")
            img = input("img 주소 입력>> ")
            print("----------------------------")        
            db_process_insert(id, title, content, director, img)
        
        elif select == '2':  
            print("### 검색할 영화 코드를 입력해주세요 ###")
            print("----------------------------")
            id = input("코드입력>> ")   
            print("----------------------------")        
            db_process_select(id)
        
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
                 
        
      
    

        
    
    
    
    
    
    
