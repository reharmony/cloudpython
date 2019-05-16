'''
Created on 2019. 5. 1.

@author: user
'''
class Dog:
    # 멤버 변수 (선언하지 않아도 생성자에 있으면 작동은 함, 하지만 선언해주는것이 정석)
    color = '';
    field = '';
     
    # 생성자
    def __init__(self, color, field):
        self.color = color
        self.field = field
    
    # 멤버 메소드
    def jump(self):
        print('뛰고 있다.')
        
    def sleep(self):
        print('자고 있다.')
        
    def __str__(self):
        return self.color + ", " + self.field


dog1 = Dog('갈색', '요크셔테리어')
print(dog1)
print(dog1.color)
print(dog1.field)

dog2 = Dog('흰색', '진돗개')
print(dog2)        
dog2.jump()
dog2.sleep()


    