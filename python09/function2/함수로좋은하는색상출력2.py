'''
Created on 2019. 4. 8.

@author: user
'''
'''
변수의 생존 범위
1. 전역변수
2. 지역변수
'''

### 좋아하는 색상 입력받아 출력하기 ###

# 리스트 정의
color=[]

# 입력함수 정의
def colorInput():
    for i in range(0,5):
        color.append(input("내가 좋아하는 색상>> "))

# 출력함수 정의
def colorList(color):
    print("내가 좋아하는 색깔은", end=" ")
    for i in color:
        print(i, end=" ")

# 메인
if __name__ == '__main__':    
     # color => main에 포함된 지역변수이다.
    colorInput()
    colorList(color)
    
    