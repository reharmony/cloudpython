'''
Created on 2019. 4. 9.

@author: user
'''
### 패스워드 생성기3 ###

import random
import string

# 영문대소문자 목록
letter = string.ascii_letters
# 10진법 정수 목록
number = string.digits
# 특수문자 목록
special = string.punctuation
# 사용할 목록 합치기
passList = letter + number + special
    
# 함수 정의
def makePass(passList, n):     
    passSelect=0
    passCount=""
    for x in range(0,n):
        for y in range(0,6):
            passSelect= random.choice(passList)
            passCount += passSelect
        print(passCount)
        passCount = ""


# 메인
if __name__ == '__main__':  
    
    makePass(passList,int(input("생성할 비밀번호의 개수입력>> ")))
    