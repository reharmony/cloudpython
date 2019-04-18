'''
Created on 2019. 4. 9.

@author: user
'''

# 전역변수
x = 300

def call():
    x = 20 # 지역변수
    print("함수 내의 x변수값(지역변수):", x)
    y = 30
    print("함수 내의 y변수값(지역변수):", y)

def call2():
    print(x)
    
    
if __name__ == '__main__':
    print("함수 밖의  x변수값(전역변수):", x)
#     print(y)
    call()
    call2()