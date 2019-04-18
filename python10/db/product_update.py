'''
Created on 2019. 4. 10.

@author: user
'''
from productDB import update


print("update 실행")
name = input("name입력>> ")
price = input("price입력>> ")
company = input("company입력>> ")
contact = input("contact입력>> ")
update(name, price, company, contact)