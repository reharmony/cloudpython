'''
Created on 2019. 4. 9.

@author: user
'''
'''
계산기의 모든 함수를 호출해서 사용
'''
import 계산기
person=0
price=0

def order():
    global person
    global price    
    person = int(input("인원수 입력>> "))
    price = int(input("커피값 입력>> "))

def totalPrice(money):
    if money > 15000:
        print("총 주문 금액은 할인을 적용하여 %d원입니다." % (money-2000))
    else:
        print("총 구문 금액은 %d원입니다." % (money))

if __name__ == '__main__':
    order()    
    money = 계산기.mul(person,price)
    totalPrice(money)
    
    