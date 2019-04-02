'''
a = 100

b = a

print(a,b)

print()
a = b = 200
print(a,b)

def sum(x, y): # x, y => 매개변수
    return x + y


a = sum(200,100)
print(a)

print("반환 받은 값>>", a)
'''

def sum2():
    x = int(input(">>"))
    y = int(input(">>"))    
    return x + y

def sum3():
    x = int(input(">>"))
    y = int(input(">>"))
    return x + y - 10


q = sum2()
print(q)

q2 = sum3()
print(q2)


