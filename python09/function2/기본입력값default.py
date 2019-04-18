'''
Created on 2019. 4. 9.

@author: user
'''
# 기본값(default) 설정하기
def call(x,y,z):
    sum = x + y + z
    print(sum/3)

def call2(x,y,z=0):
    sum = x + y + z
    print(sum/3)

if __name__ == '__main__':
    call(100,80,50)
    
    call2(100,80)
    call2(100,80,50)