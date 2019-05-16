'''
Created on 2019. 5. 1.

@author: user
'''
class Tv:
    color = ''
    size = 0
    count = 0
    
    def __init__(self, color, size):
        self.color = color
        self.size = size
        Tv.count = Tv.count + 1
        # 클래스당 하나만 존재함
        # 생성된 객체간 공유 가능한 클래스 변수(static)
    
    
    def changeCh(self, ch):
        print(str(ch) + "번 채널로 변경하다.")
    
    def powerOff(self):
        pass
    
    def __str__(self):
        return self.color + " " + str(self.size)
    
myTv = Tv('빨강', 50)
print(myTv)
print(Tv.count)

yourTv = Tv('파랑', 100)
print(yourTv)
print(Tv.count)
    
