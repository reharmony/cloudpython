'''
Created on 2019. 5. 2.

@author: user
'''
class 통신부품:
    def send(self):
        pass
    
    def receive(self):
        pass
    
class 채팅(통신부품):
    def send(self):
        return '안녕..!!!'