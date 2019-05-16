'''
Created on 2019. 5. 2.

@author: user
'''

class Shape:
    name = 'ok'
    
    def fun1(self): # 일반메소드
        print('함수1 호출되다.')
        
    def fun2(self): # 추상메소드 (아직 기능이 정의되지 않음)
        pass

s1 = Shape()
s1.fun1()
s1.fun2()