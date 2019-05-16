'''
Created on 2019. 4. 10.

@author: user
'''
import pymysql

def db_process_insert(id, pw, name, tel):
    
    # 1. db인증 -> 연결
    con = pymysql.connect(host ='localhost', user='root',password='1234', db = 'cloud')
    print("1. db인증 -> 연결 성공...")
    print(con)
    
    # 2. 연결정보 -> 통로
    cur = con.cursor()
    print()
    print("2. 연결정보 -> 통로 만들기 성공...")
    
    # 3. sql문 만들어서 -> 전송
    sql = "update member set pw =" + pw + ", name ="+ name +", tel=" + tel + " where id=" + id
#     sql = "insert into member values ('444','444','444')"
#     sql1 = "insert into member values ('111','111','111','111')"
#     sql2 = "insert into member values ('222','222','222','222')"
#     sql3 = "insert into member values ('333','333','333','333')"
    cur.execute(sql)
#     result1 = cur.execute(sql1)
#     result2 = cur.execute(sql1)
#     result3 = cur.execute(sql3)
#     print(result1)
#     print(result2)
#     print(result3)
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
    sql = "select * from member where id = " + id
#     sql = "select * from member"
    result = cur.execute(sql)
    print(result) # 가져온 레코드의 개수 표시
    print("3. sql문 만들어서 -> 전송 성공...")
    record = cur.fetchone() # record 변수에 결과값이 튜플 형식으로 저장됨
    print("검색된 ID:",record[0])
    print("검색된 PW:",record[1])
    print("검색된 NAME:",record[2])
    print("검색된 TEL:",record[3])
    print()
    con.commit()
    
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
    sql = "update member set pw =" + pw + ", name ="+ name +", tel=" + tel + " where id=" + id
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
    sql = "delete from member where id =" + id
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
        print("##### DB 관리 프로그램 ###")
        select = input("1.가입  2.검색 3.수정 4.삭제 0.종료 >> ")
          
        if select == '1':  
            print("### 회원가입 정보를 입력해주세요 ###")
            print("----------------------------")
            id = input("ID입력>> ")
            pw = input("PW입력>> ")
            name = input("NAME입력>> ")
            tel = input("TEL입력>> ")
            print("----------------------------")        
            db_process_insert(id, pw, name, tel)
        
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
    
        elif select == '0':  
            print("### DB프로그램을 종료합니다. ###")
            break
        
        else :
            print("잘못된 번호입니다. 다시 입력해주세요.")
            print("----------------------------")        
                 
        
      
    

        
    
    
    
    
    
    
