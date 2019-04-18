'''
Created on 2019. 4. 9.

@author: user
'''
# CRUD문 순서 

def create(id, title, content, writer):
    print("1. DB연결, 인증(id/pw)")
    sql = "insert into bbs values (%s, %s, %s, %s)" % (id, title, content, writer)    
    print("2. %s 문 실행 요청" % sql)
    print("3. DB연결 해제")

def read(id):
    print("1. DB연결, 인증(id/pw)")    
    sql = "select * from bbs where id=" + id    
    print("2. %s 문 실행 요청" % sql)
    print("3. 검색결과를 받아와서 처리")
    print("4. DB연결 해제")
#     return "select한 결과 반환"
    id = 100
    title = 200
    content = 300
    writer = 400
    return id, title, content, writer
#     result = []
#     result.append(100)
#     result.append(200)
#     result.append(300)
#     result.append(400)
#     return result
    
def update(id, title, content, writer):
    print("1. DB연결, 인증(id/pw)")
    sql = "update bbs set content = '%s' where id = '%s'" % (content, id)    
    print("2. %s 문 실행 요청" % sql)
    print("3. DB연결 해제")
    
def delete(title):
    print("1. DB연결, 인증(id/pw)")
    sql = "delete from bbs where title = '%s'" % title  
    print("2. %s 문 실행 요청" % sql)
    print("3. DB연결 해제")
    
    