'''
Created on 2019. 4. 8.

@author: user
'''
# 좋아하는 색상 입력받아 출력하기

# 출력함수 정의
def colorList(color):
    print("내가 좋아하는 색깔은", end=" ")
    for i in color:
        print(i, end=", ")

# 메인
if __name__ == '__main__':    
    color=[]
    for i in range(0,5):
        color.append(input("내가 좋아하는 색상>> "))
    colorList(color)
    
    