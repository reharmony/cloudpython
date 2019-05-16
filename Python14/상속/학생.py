'''
Created on 2019. 5. 2.

@author: user
'''

class Student:
    name = 0
    age = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def learn(self):
        print(self.name + '이(가) 공부하고 있다.')
    
    def eat(self):
        print(self.name + '이(가) 급식을 먹고 있다.')
        

class Elementary(Student):
    
    def __init__(self, name, age):
        Student.__init__(self, name, age)
        self.name = name
        self.age = age
        
    def learn(self):
        print(self.name + '이(가) 슬기로운 생활을 공부하고 있다.')
        
    def __str__(self):
        return "%s\t%s\t" % (self.name,self.age)


class Middle(Student):
    
    def __init__(self, name, age):
        Student.__init__(self, name, age)
        self.name = name
        self.age = age
        
    def learn(self):
        print(self.name + '이(가) 기술가정을 공부하고 있다.')
        
    def __str__(self):
        return "%s\t%s\t" % (self.name,self.age)


class High(Student):
    
    def __init__(self, name, age):
        Student.__init__(self, name, age)
        self.name = name
        self.age = age
        
    def learn(self):
        print(self.name + '이(가) 수학의 정석을 공부하고 있다.')
        
    def __str__(self):
        return "%s\t%s\t" % (self.name,self.age)
    
    
child1 = Elementary('Tom', '9')
child2 = Middle('Tony', '15')
child3 = High('Stark', '18')

print('이름\t나이')
print(child1)
print(child2)
print(child3)

child1.eat()
child1.learn()
child2.learn()
child3.learn()