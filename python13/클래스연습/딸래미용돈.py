'''
Created on 2019. 5. 1.

@author: user
'''
class Money:
    name = '';
    age = 0
    give = 10000
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Money.give = Money.give - 1000
   
    def play(self):
        print(self.name + "이(가) 놀고 있어요.")
    
    def watch(self):
        print(self.name + "이(가) TV를 보고 있어요.")
        
    def __str__(self):
        return "딸의 이름은 " + self.name + "입니다."
    
if __name__ == '__main__':
    daughter1 = Money('Ami', 11)
    print(daughter1)
    daughter1.play()
    print("아빠의 지갑엔 ", Money.give, "원이 남았어요.")
    
    print()
    
    daughter2 = Money('Lily', 13)    
    print(daughter2)
    daughter2.watch()
    print("아빠의 지갑엔 ", Money.give, "원이 남았어요.")