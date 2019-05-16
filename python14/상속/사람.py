'''
Created on 2019. 5. 2.

@author: user
'''

class Person:
    name = ''
    age = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def sleep(self):
        print(self.name + "(이)가 자고 있어요.")
        
    def eat(self):
        print(self.name + "(이)가 식사를 하고 있어요.")
        
class Man(Person):
    power_size = 10
    
    def __init__(self, name, age, power_size):
        Person.__init__(self, name, age)
        self.name = name
        self.age = age
        self.power_size = "힘:%d" % power_size
        
    def fast_run(self):
        print(self.name + "(이)가 빠르게 달리고 있어요.")

man1 = Man('James', 24, 120)
man2 = Man('Poter', 21, 100)

print(man1.name, man1.age, "세")
man1.sleep()
man1.eat()
man1.fast_run()
print(man1.power_size)

print()

print(man2.name, man2.age, "세")
man2.sleep()
man2.eat()
man2.fast_run()
print(man2.power_size)

        
    