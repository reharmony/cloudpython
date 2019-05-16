'''
Created on 2019. 4. 9.

@author: user
'''
import 회원db처리


if __name__ == '__main__':
    
    choose = int(input("이용할 서비스를 입력하세요(1=C / 2=R / 3=U / 4=D)>> "))
              
    if choose == 1:
    # create
        print("### 회원 가입 ###")
        id = input("id를 입력하세요>> ")
        pw = input("pw를 입력하세요>> ")
        name = input("이름을 입력하세요>> ")
        gender = input("성별을 입력하세요>> ")
        
        회원db처리.create(id, pw, name, gender)
        
    if choose == 2:
    # select
        print("### 회원 정보 검색 ###")
        id = input("id를 입력하세요>> ")
        
        회원db처리.read(id)
#         a, b, c, d = 회원db처리.read(id)
#         print(a, b, c, d)
        
    if choose == 3:
    # update
        print("### 회원 가입 ###")
        id = input("id를 입력하세요>> ")        
        name = input("이름을 입력하세요>> ")        
        
        회원db처리.update(id, name)
        
    if choose == 4:
    # delete
        print("### 회원 가입 ###")
        id = input("id를 입력하세요>> ")        
        
        회원db처리.delete(id)


