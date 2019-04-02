'''
name = [] # 비어있는 리스트

print(name)

name.append("김아무개")
name.append("박아무개")

print(name)

data = input("이름을 입력>> ")
name.append(data)

print(name)
'''
name2=[]
for i in range(0,5):
    data2 = input("이름을 입력하세요>> ")
    name2.append(data2)
    
print(name2)
    
for i in range(0,len(name2)):
    print(name2[i])