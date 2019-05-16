'''
Created on 2019. 4. 9.

@author: user
'''

# create
def create(id, pw, name, gender):
    print("1. DB연결")
    sql = "INSERT INTO people values (%s, %s, %s, %s)" % (id, pw, name, gender)
    print("2. %s 문 실행 요청" % sql)
    print("3. DB연결 해제")
    print("4. 회원가입이 완료되었습니다.")

# read
def read(id):
    print("1. DB연결")
    sql = "SELECT * FROM people WHERE id ='%s" % id
    print("2. %s 문 실행 요청" % sql)
    print("3. DB연결 해제")
    id = 'id'
    pw = 'pw'
    name = 'name'
    gender = 'gender'
#     return id, pw, name, gender
    return ['id','pw','name','gender']
    
    
# update
def update(id, name):
    print("1. DB연결")
    sql = "UPDATE people SET name ='%s' WHERE id ='%s'" % (name, id)  
    print("2. %s 문 실행 요청" % sql)
    print("3. DB연결 해제")
    print("4. 회원정보 수정이 완료되었습니다.")

# delete
def delete(id):
    print("1. DB연결")
    sql = "DELETE FROM people WHERE ID ='%s'" % id
    print("2. %s 문 실행 요청" % sql)
    print("3. DB연결 해제")
    print("4. 회원정보 삭제가 완료되었습니다.")
    
    