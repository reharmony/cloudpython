'''
Created on 2019. 4. 10.

@author: user
'''
import pymysql

# Main_UI 핫무비와 박스오피스에 표시할 정보 가져오기
def db_process_select(selectday):
    
    # 1. db인증 -> 연결
    con = pymysql.connect(host ='13.209.92.229', user='root',password='1234', db = 'cloud')
    print("1. db인증 -> 연결 성공...")
    print(con)
    
    # 2. 연결정보 -> 통로
    cur = con.cursor()
    print()
    print("2. 연결정보 -> 통로 만들기 성공...")
    
    # 3. sql문 만들어서 -> 전송
#     for rank in range(1,2):
    box_list=[]
    for rank in range(1,11):
        sql = "select title, people, poster from movieinfo where title in (select title from boxoffice where selectday ='" + selectday + "' and rank =%s)" % str(rank)    
        print()
        print("3. sql문 만들어서 -> 전송 성공...")
        cur.execute(sql)
        searching = cur.fetchone() # 레코드 여러개 조회시 fetchall -> 반복문사용
#         print("----------------------------")
#         print("moviecode")
#         print("----------------------------")
#         print(searching)
        box_list.append(searching)
#     print(box_list)
#     for x in searching:
#         print(x)    
#     print("\n----------------------------")
    con.commit()
    print (box_list)
    return box_list

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
     
        if select == '2':  
            print("### 검색할 박스오피스의 기준날짜를 입력해주세요 ###")
            print("----------------------------")
            selectday = input("날짜입력(ex.20190101)>> ")   
            print("----------------------------")        
            db_process_select(selectday)

        elif select == '0':  
            print("### 영화 정보 관리 프로그램을 종료합니다. ###")
            break
        
        else :
            print("잘못된 번호입니다. 다시 입력해주세요.")
            print("----------------------------")        
                 
        
      
    

        
    
    
    
    
    
    
