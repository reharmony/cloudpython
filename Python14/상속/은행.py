'''
Created on 2019. 5. 2.

@author: user
'''

class Bank:
    def 대출이자를받다(self):
        return 0
    
class Bad_bank(Bank):
    def 대출이자를받다(self):
        return 0.1
#         print("Bad_bank의 이자는 %d%%입니다." % 10)
    
class Normal_bank(Bank):
    def 대출이자를받다(self):
        return 0.05
#         print("Normal_bank의 이자는 %d%%입니다." % 5)

class Good_bank(Bank):
    def 대출이자를받다(self):
        return 0.02
#         print("Good_bank의 이자는 %d%%입니다." % 2)
    
bank1 = Bad_bank()
bank2 = Normal_bank()
bank3 = Good_bank()

print(bank1.대출이자를받다())
print(bank2.대출이자를받다())
print(bank3.대출이자를받다())

# bank1.대출이자를받다()
# bank2.대출이자를받다()
# bank3.대출이자를받다()