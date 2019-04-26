import pymysql


def member_Login(id, pw):
    con = pymysql.connect(host ='13.209.92.229', user = 'root', password = '1234', db = 'cloud')
    print('DB인증 >> 연결 성공...')
    print(con)
    
    
    cur = con.cursor()
    print(cur)
    
   
    sql = "select * from member where id = ('" + id + "')and pw = ('" + pw + "')"
    
    result = cur.execute(sql)
    print('sql문 실행결과: ', result)
    print('전송 성공')
    con.commit()
    
    recode = cur.fetchone()
    
    print(recode[0], recode[1]) 
    
    con.close()
    print('연결해제')
    return recode