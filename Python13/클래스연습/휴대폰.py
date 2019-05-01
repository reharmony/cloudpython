'''
Created on 2019. 5. 1.

@author: user
'''
class Phone:
    color = '';
    company = '';
    
    def search(self):
        print('인터넷 검색.')
        
    def picture(self):
        print('사진찍기.')
    
    def __str__(self):
        return self.color + " " + self.company

p1 = Phone()
p1.color = '빨강'
p1.company = 'SK'

p2 = Phone()
p2.color = '노랑'
p2.company = 'LG'

p3 = Phone()
p3.color = '파랑'
p3.company = '삼성'

p1.picture()
p2.search()
p3.picture()

print(p1)
print(p2)
print(p3)