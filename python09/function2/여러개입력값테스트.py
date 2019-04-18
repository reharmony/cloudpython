'''
Created on 2019. 4. 9.

@author: user
'''
# 값 개수 상관없이 자유롭게 넘기기 (튜플 이용)

def call(*parameter):
    print("전달 받은 데이터 개수:",len(parameter))
    for x in parameter:
        print(x, end=" ")
    print()

if __name__ == '__main__':
    call(1,2,3,4,5)
    call(1,2,3,4)
    call(1,2,3)