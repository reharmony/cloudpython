'''
Created on 2019. 4. 10.

@author: user
'''
import pymysql

def insert(name, price, company, contact):
    # 1. DB인증
    con = pymysql.connect(host = 'localhost', user = 'root', password = '1234', db = 'shop')
    print()
    print("===========================")
    print()
    print("1. DB인증 -> 연결성공")
    print(con)
    print()
    
    # 2. 연결 통로 만들기
    cur = con.cursor()
    print("2. 연결 -> 통로 만들기 성공")    
    print()
    
    # 3. SQL문 전송
    sql = 'insert into product values (%s, %s, %s, %s)' % (name, price, company, contact)
    cur.execute(sql)
    con.commit()
    print("3. sql문 만들어서 -> 전송")
    print()

    # 4. DB 연결해제
    print("4. DB 연결해제")
    con.close()
    print()
    print("===========================")
    print()
    
    
def select(name):
    # 1. DB인증
    con = pymysql.connect(host = 'localhost', user = 'root', password = '1234', db = 'shop')
    print("1. DB인증 -> 연결성공")
    print(con)
    print()
    
    # 2. 연결 통로 만들기
    cur = con.cursor()
    print("2. 연결 -> 통로 만들기 성공")    
    print()
    
    # 3. SQL문 전송
    sql = 'select * from product where name =' + name
    cur.execute(sql)
    result = None
    result = cur.fetchone()    
    con.commit()
    print("3. sql문 만들어서 -> 전송")
    print("--------------------------")
    print("name\tprice\tcompany\tcontact")
    print("--------------------------")
    for i in result:
        name = result[0]
        price = result[1]
        company = result[2]
        contact = result[3]
    print("%s\t%s\t%s\t%s" % (name, price, company, contact))
    con.commit()      
    print()     
    
    
    # 4. DB 연결해제
    print("4. DB 연결해제")
    con.close()
    print()
    print("===========================")
    print()
    
    
def update(name, price, company, contact):
    # 1. DB인증
    con = pymysql.connect(host = 'localhost', user = 'root', password = '1234', db = 'shop')
    print("1. DB인증 -> 연결성공")
    print(con)
    print()
    
    # 2. 연결 통로 만들기
    cur = con.cursor()
    print("2. 연결 -> 통로 만들기 성공")    
    print()
    
    # 3. SQL문 전송
    sql = 'update product set price = %s, company = %s, contact = %s where name = %s' % (price, company, contact, name)
    cur.execute(sql)
    con.commit()
    print("3. sql문 만들어서 -> 전송")
    print()

    # 4. DB 연결해제
    print("4. DB 연결해제")
    con.close()
    print()
    print("===========================")
    print()
    
    
def delete(name):
    # 1. DB인증
    con = pymysql.connect(host = 'localhost', user = 'root', password = '1234', db = 'shop')
    print("1. DB인증 -> 연결성공")
    print(con)
    print()
    
    # 2. 연결 통로 만들기
    cur = con.cursor()
    print("2. 연결 -> 통로 만들기 성공")    
    print()
    
    # 3. SQL문 전송
    sql = 'delete from product where name=' + name
    cur.execute(sql)
    con.commit()
    print("3. sql문 만들어서 -> 전송")
    print()

    # 4. DB 연결해제
    print("4. DB 연결해제")
    con.close()
    print()
    print("===========================")
    print()
    

    