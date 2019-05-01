'''
Created on 2019. 5. 1.

@author: user
'''
### 우리집 계좌 ###
class Account:
    product = '';
    name = '';
    money = '';
    
    def __init__(self, product, name, money):
        self.product = product
        self.name = name
        self.money = money
        
        
acc1 = Account('청약저축', '김아무개', 500)
acc2 = Account('내비상금', '김아무개딸', 30)
acc3 = Account('자유적금', '박아무개', 100)

print("---------------------------------------")
print(acc2.product, "통장에는", acc2.money,"만원이 들어있어요.")
print(acc3.name, "통장에는", acc3.money,"만원이 들어있어요.")
print()
print("우리집 전체 예금액은", acc1.money + acc2.money + acc3.money, "만원이에요!")
print("---------------------------------------")
