'''
Created on 2019. 5. 1.

@author: user
'''
### 관리자 계정 관리 ###
class Member:
    id = '';
    pw = '';
    grade = ''; 
    mileage = '';
    
    def __init__(self, id, pw, grade, mileage):
        self.id = id
        self.pw = pw
        self.grade = grade
        self.mileage = int(mileage)
 
if __name__ == '__main__':
    
    id = input("아이디를 입력하세요.>> ")
    pw = input("비밀번호를 입력하세요.>> ")
    grade = input("등급을 입력하세요.>> ")
    mileage = input("마일리지를 입력하세요.>> ")
    
    mem1 = Member(id, pw, grade, mileage)
    
    id = input("아이디를 입력하세요.>> ")
    pw = input("비밀번호를 입력하세요.>> ")
    grade = input("등급을 입력하세요.>> ")
    mileage = input("마일리지를 입력하세요.>> ")
    
    mem2 = Member(id, pw, grade, mileage)
    
    id = input("아이디를 입력하세요.>> ")
    pw = input("비밀번호를 입력하세요.>> ")
    grade = input("등급을 입력하세요.>> ")
    mileage = input("마일리지를 입력하세요.>> ")
    
    mem3 = Member(id, pw, grade, mileage)
    
    print("-------------------------------------")
    print(mem1.id, "의 비밀번호는", mem1.pw, "입니다.")
    print(mem2.id, "는", mem2.grade, "이고 마일리지는", mem2.mileage, "입니다.")
    print("총 마일리지는", mem1.mileage + mem2.mileage + mem3.mileage, "입니다.")
    print("평균 마일리지는", int((mem1.mileage + mem2.mileage + mem3.mileage)/3), "입니다.")

    
    
    
    