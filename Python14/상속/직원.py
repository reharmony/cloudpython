'''
Created on 2019. 5. 2.

@author: user
'''

class Employee:
    name = ''
    inum = ''
    phone = ''
    dept = ''
    age = ''
    
    def __init__(self, name, inum, phone, dept, age):
        self.name = name
        self.inum = inum
        self.phone = phone
        self.dept = dept
        self.age = age
    
    def work(self):
        print(self.name + "이(가) 일하고 있다.")
        
    def talk(self):
        print(self.name + "이(가) 대화하고 있다.")
   
        
class Manager(Employee):
    admin_dept = ''
    
    def __init__(self, name, inum, phone, dept, age, admin_dept):
        Employee.__init__(self, name, inum, phone, dept, age)
        self.name = name
        self.inum = inum
        self.phone = phone
        self.dept = dept
        self.age = age
        self.admin_dept = admin_dept
    
    def admin(self):
        print(self.name + "이(가) 관리감독하고 있다.")
         
    def __str__(self):
        return "%s\t%s\t%s\t%s\t%s\t%s" % (self.name,self.inum,self.phone,self.dept,self.age,self.admin_dept)
        
man1 = Manager('John', '920108', '01012345678', 'account', '28', 'account2')
man2 = Manager('Smith', '950512', '01095876263', 'supply', '25', 'supply3')

print('이름\t주민번호\t전화번호\t\t소속부서\t나이\t담당부서')
print(man1)
print(man2)
man1.work()
man2.admin()
man1.talk()



    
    
    
    
    