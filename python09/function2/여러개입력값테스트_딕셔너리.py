'''
Created on 2019. 4. 9.

@author: user
'''
'''
Created on 2019. 4. 9.

@author: user
'''
# 값 개수 상관없이 자유롭게 넘기기 (딕셔너리 이용)

def call(**parameter):
    print("전달 받은 데이터 개수:",len(parameter))
    for x in parameter.keys():
        print(x, ":", parameter[x], end="")
        print()

if __name__ == '__main__':
    call(감자=20,고구마=40,양파=60)
 
