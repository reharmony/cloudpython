'''
Created on 2019. 5. 1.

@author: user
'''
class Employee:
    name = ''
    gender = ''
    age = ''
    agesum = 0
    empcnt = 0
    ageavg = 0
    
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        Employee.agesum = Employee.agesum + self.age
        Employee.empcnt = Employee.empcnt + 1 
        Employee.ageavg = self.agesum / self.empcnt
        
    def work(self):
        print(self.name + "이(가) 일하다.")
        
    def insider(self):
        print(self.name + "은(는) 친화력이 있다.")
    
    def __str__(self):
        return "직원수:" + str(self.empcnt) +  "\n평균나이:" + str(int(Employee.ageavg)) + "세"
       
    
if __name__ == '__main__':
    
    emp1 = Employee('James', 'male', 27)
    emp2 = Employee('Lisa', 'female', 23)
    emp3 = Employee('John', 'male', 25)
    
    emp1.work()
    emp2.insider()
    
    print(emp3)