'''
Created on 2019. 4. 8.

@author: user
'''
'''
1. 더하기
2. 빼기
3. 곱하기
4. 나누기
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
    z = x / y
    print("두 수의 나눗셈은", z)
    
if __name__ == '__main__':
    print("나의 계산기가 시작됩니다.")
    x = int(input("숫자1>> "))
    y = int(input("숫자2>> "))
    
    addNum(x,y)
    minusNum(x, y)
    multiNum(x, y)
    divNum(x, y)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    