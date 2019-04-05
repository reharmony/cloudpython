number = [1,2,3,4,5]

# for문으로 리스트 출력하기
for i in range(0,len(number)):
    print(number[i])

print("-----------")

# while문으로 리스트 출력하기
i = 0
while i < len(number):
    print(number[i])
    i = i + 1

print("-----------")

# 1~10 더하기
sum = 0
for i in range(1,11):
    sum = sum + i
    if i < 10:
        print(i, "+ ", end="")
    else:
        print(i, "= ", end="")
print(sum)

print("-----------")

# 1~100 더하기
sum = 0
for i in range(1,101):
    sum = sum + i
print("1 + 2 + ... + 99 + 100 = ", end="")
print(sum)

print("-----------")

# 1~1000 더하기
sum = 0
for i in range(1,1001):
    sum = sum + i
print("1 + 2 + ... + 999 + 1000 = ", end="")  
print(sum)

print("-----------")

# 1~10000 더하기
sum = 0
for i in range(1,10001):
    sum = sum + i
print("1 + 2 + ... + 9999 + 10000 = ", end="")  
print(sum)

print("-----------")

# for문으로 리스트에 값 삽입하기 (1~10)
ten=[]
for i in range(1,11):
    ten.append(i)
print(ten)

print("-----------")

# 입력받은 값 리스트에 삽입하기
data_list=[]
for x in range(0,10):
    data = int(input("숫자입력>> "))
    data_list.append(data)
print(data_list)

print("-----------")

# 리스트에 있는 값 더하기
sum = 0
for x in range(0,10):
    sum = sum + data_list[x] 
print(sum)

print("-----------")

# while문으로 리스트에 값 삽입하기
ten2=[]
x = 1
while x < 11:
    ten2.append(x)
    x += 1
print(ten2)

