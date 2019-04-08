'''
Created on 2019. 4. 8.

@author: user
'''

'''
<커피전문점에 필요한 함수>
1. 총 커피값: 인원 * 커피값
2. 총 지불금액: 인원 * 커피값이 15000원 초과시 할인 2000원 (할인여부 판단)
'''
def coffeeSum(person,price):
    sum = person * price
    return  sum # return 받는 대상: main 함수

def coffeeSale(sum):
    if sum > 15000:
        print("당신이 지불할 커피 금액은", sum-2000, "원")
    else:
        print("당신이 지불할 커피 금액은", sum, "원")


if __name__ == '__main__':
    person = int(input("인원 입력>> "))
    price = int(input("커피값 입력>> "))
    
    sum = coffeeSum(person,price)
    coffeeSale(sum)
    
    