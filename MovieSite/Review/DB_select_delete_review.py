import pymysql

def review_insert(reviewtitle, reviewcontent, id, title):
    con = pymysql.connect(host ='13.209.92.229', user = 'root', password = '1234', db = 'cloud')
    print('연결 성공')
    print(con)
    cur = con.cursor()
    print(cur)
    sql = "insert into reviewboard (reviewtitle, reviewcontent, id , title) values ('" + reviewtitle + "', '" + reviewcontent + "', '" + id + "', '" + title + "')"
    print('생성된sql: ', sql)
    cur.execute(sql)
    print('전송 성공')
    con.commit()
    con.close()
    print('연결해제')
    
def review_select(boardnum):
    con = pymysql.connect(host ='13.209.92.229', user = 'root', password = '1234', db = 'cloud')
    print('연결 성공')
    print(con)
    cur = con.cursor()
    print(cur)
    sql = "select * from reviewboard where boardnum =" + boardnum
    result = cur.execute(sql)
    print('sql문 실행결과: ', result)
    print('전송 성공')
    con.commit()
    recode = cur.fetchone()
    print(recode[0], recode[1], recode[2], recode[3], recode[4]) 
    con.commit()
    con.close()
    print('연결해제')

def review_delete(boardnum):
    con = pymysql.connect(host ='13.209.92.229', user = 'root', password = '1234', db = 'cloud')
    print('연결 성공')
    print(con)
    cur = con.cursor()
    print(cur)
    sql = "delete from reviewboard where boardnum =" + boardnum
    print(sql)
    cur.execute(sql)
    print('전송 성공')
    con.commit()
    con.close()
    print('연결해제')


    
