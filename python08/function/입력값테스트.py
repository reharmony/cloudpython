'''
Created on 2019. 4. 8.

@author: user
'''
# 1. 더하기 함수
def addNum(x,y): # x, y : 매개변수
    z = x + y # x,y,z는 지역변수 이기 때문에 다른 함수에서도 같은 이름을 사용 가능
    print("두 수의 합은",z)
    
# 2. 빼기 함수
def minusNum(x,y):
    z = x - y
    print("두 수의 차는", z)
    
# 3. 곱하기 함수
def multiNum(x,y):
    z = x * y
    print("두 수의 곱은", z)
    
# 4. 나누기 함수
def divNum(x,y):
    if y == 0:
        print("0으로 나눌 수 없습니다.")
    else:
        z = x / y
        print("두 수의 나눗셈은", z)
    
# 5. 제곱 함수
def double(x,y):
    z = x ** y
    print("두 수의 제곱은", z)

if __name__ == '__main__':
    # 입력받기
    x = int(input("첫번째 숫자 입력>> "))
    c = input("계산을 입력하세요(+,-,*,/,**)>> ")
    y = int(input("두번째 숫자 입력>> "))
    
    # 연산자 판별 
    if c == '+':
        addNum(x, y)
    elif c == '-':
        minusNum(x, y)
    elif c == '*':
        multiNum(x, y)
    elif c == '/':
        divNum(x, y)
    elif c == '**':
        double(x, y)
    else:
        print("잘못된 연산자입니다.")
    
    ## 다중 입력 받기
#     e, f = input("값을 입력>> ").split(",") 
#     입력시 split 안의 ","를 이용해 나눠서 입력 ex) 3,5
#     split의 기본 구분 기호는 공백 ("")
#     print(e)
#     print(f)