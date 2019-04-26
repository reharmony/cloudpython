import pymysql
data = None
def insert_member(id, pw, name, tel, email, birth, gender):
    con = pymysql.connect(host ='13.209.92.229', user = 'root', password = '1234', db = 'cloud')
    print('연결 성공')
    print(con)
    cur = con.cursor()
    print(cur)
    sql = "insert into member (id, pw, name, tel, email, birth, gender) values ('"+ id + "', '" + pw + "', '" + name + "', '" + tel +"', '" + email + "', '" + birth + "', '" + gender + "')"
    print(data)
    cur.execute(sql)
    print('전송 성공')
    con.commit()
    con.close()
    print('연결해제')
    
def member_update(pw, name, tel, email, birth, id):
    con = pymysql.connect(host ='13.209.92.229', user = 'root', password = '1234', db = 'cloud')
    print('연결 성공')
    print(con)
    cur = con.cursor()
    print(cur)
    sql = "update member set pw =('" + pw + "'), name =('" + name + "'), tel =('" + tel + "'), email =('" + email + "'), birth =('" + birth + "') where id =('" + id + "')"
    cur.execute(sql)
    print('전송 성공')
    con.commit()
    con.close()
    print('연결해제')

def member_delete(id):
    con = pymysql.connect(host ='13.209.92.229', user = 'root', password = '1234', db = 'cloud')
    print('연결 성공')
    print(con)
    cur = con.cursor()
    print(cur)
    sql = "delete from member where id =('" + id +"')"
    cur.execute(sql)
    print('전송 성공')
    con.commit()
    con.close()
    print('연결해제')
    
    
if __name__ == '__main__':
    print(data)
    