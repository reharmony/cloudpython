'''
Created on 2019. 5. 2.

@author: user
'''

class Human:
    name = ''
    age = ''
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        print(self.name + "이(가) 밥을 먹는다.")

    def sleep(self):
        print(self.name + "이(가) 잠을 잔다.")
        
    
class Woman(Human):
    size = ''
    hair = ''
    
    def __init__(self, name, age, size, hair):
        Human.__init__(self, name, age)
        self.name = name
        self.age = age
        self.size = size
        self.hair = hair
    
    def beauty(self):
        print(self.name + "이(가) 화장을 한다.")
        
    def hairing(self):
        print(self.name + "이(가) 머리를 손질하고 있다.")
    
    def __str__(self):
        return "%s\t%s\t%s\t%s" % (self.name,self.age,self.size,self.hair)
    

class Wonderwoman(Woman):
    power = ''
    speed = ''
    
    def __init__(self, name, age, size, hair, power, speed):
        Woman.__init__(self, name, age, size, hair)
        self.name = name
        self.age = age
        self.size = size
        self.hair = hair
        self.power = power
        self.speed = speed
    
    def shield(self):
        print(self.name + "이(가) 방패를 들어서 방어하고 있다.")
    
    def whip(self):
        print(self.name + "이(가) 진실의 채찍을 휘두르고 있다.")
    
    def __str__(self):
        return "%s\t%s\t%s\t%s\t%s\t%s" % (self.name,self.age,self.size,self.hair,self.power,self.speed)
    
    
people1 = Woman('Lily', '19', '44', 'blond')
people2 = Wonderwoman('Cathy', '25', '55', 'black', '100', '200')

print("이름\t나이\t사이즈\t헤어\t파워\t스피드")
print(people1)
print(people2)

people1.eat()
people1.beauty()

people2.sleep()
people2.hairing()
people2.shield()
people2.whip()

 
    

