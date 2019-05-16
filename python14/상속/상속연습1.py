'''
Created on 2019. 5. 2.

@author: user
'''
#슈퍼=부모클래스
#자식=서브클래스


class Car:
    color = '검정색'
    speed = 100
    
    def speed_up(self):
        print('속도를 Up')
    
    def speed_down(self):
        print('속도를 Down')
        
# class 서브클래스(슈퍼클래스):
class Truck(Car):
    적재량 = 1
    
    def 적재량알아보기(self):
        return self.적재량
    

truck1 = Truck()
print(truck1.color) # Car의 변수
print(truck1.speed) # Car의 변수
print(truck1.적재량) # Truck의 변수

truck1.speed_up()
truck1.speed_down()
print(truck1.적재량알아보기())
