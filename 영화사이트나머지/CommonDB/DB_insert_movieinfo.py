#-*- coding:utf-8 -*-

'''
Created on 2019. 4. 10.

@author: user
'''
import pymysql
from CommonDB.Final_Total import totalinfo  
from string import ascii_uppercase

# 기준일의 전체영화정보 불러오기
def import_totalinfo():
    all = totalinfo()
    print("all\n", all)
    for i in range(0,10):
        one = all[i]
        print(one)    
        selectday = one[0]
        rank = one[1]            
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
        db_process_insert(selectday, rank, moviecode, title, engtitle, openday, people, runningtime, age, genre, director, actor, poster, star)


# 기준일 박스오피스 10위권의 영화정보 DB에 입력
def db_process_insert(selectday, rank, moviecode, title, engtitle, openday, people, runningtime, age, genre, director, actor, poster, star):
    
    # 1. db인증 -> 연결
    con = pymysql.connect(host ='13.209.92.229', user='root',password='1234', db = 'cloud')
    print("1. db인증 -> 연결 성공...")
    print(con)
    
    
    
    
    # 2. 연결정보 -> 통로
    cur = con.cursor()
    print()
    print("2. 연결정보 -> 통로 만들기 성공...")
    
    
    
    
    # 3. sql문 만들어서 -> 전송
    
    ## 영화상세정보 입력 
    try:
        sql = "insert into movieinfo values ('" + title + "','" + engtitle + "','" + openday + "','" + people + "','" + runningtime + "','" + age + "', '" + genre + "', '" + director + "', '" + actor + "', '" + poster + "','" + star + "')"
        cur.execute(sql)
        con.commit()
        print("3. 영화상세정보 전송 성공...")
    except:
        pass  
        print("3. 중복된 영화상세정보 Pass...")
    
    ## 박스오피스 정보입력
    try:  
        sql = "insert into boxoffice values ('" + selectday + "','" + rank + "','"+ title + "')"
        cur.execute(sql)
        con.commit()
        print("3. 박스오피스 정보 전송 성공...")
    except:
        pass
        print("3. 중복된 박스오피스 정보 Pass...")   
    
    
    
        
    
    
    # 4. db연결해제
    con.close()
    print()
    print("4. db 연결해제 성공...")
    print("===============================")   
    print()
   
   
   

if __name__ == '__main__':
   
    while True :
        print("##### 영화정보 DB 관리 프로그램 #####")
        select = input("1.입력  2.검색 3.수정 4.삭제 0.종료 >> ")
          
        if select == '1':  
            print("### 일일 박스오피스 영화 정보를 DB에 전송합니다. ###")
            print("----------------------------")
           
            all = totalinfo()
            for i in range(0,10):
                one = all[i]
                print(one)    
                selectday = one[0]
                rank = one[1]            
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
                db_process_insert(selectday, rank, moviecode, title, engtitle, openday, people, runningtime, age, genre, director, actor, poster, star)
                
            print("----------------------------")        
 
        elif select == '0':  
            print("### DB프로그램을 종료합니다. ###")
            break
        
        else :
            print("잘못된 번호입니다. 다시 입력해주세요.")
            print("----------------------------")        
                 
        
      
    

        
    
    
    
    
    
    
