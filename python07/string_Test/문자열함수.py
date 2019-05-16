data = "파이썬은 아주 Easy!!! but High..."

print(data.upper())
print(data.lower())
print(data.swapcase())
print(data.title())

print("------------------")

print(len(data))
print(data.count('!'))
print(data.find('아주'))
print(data.rfind('아주'))
print(data.startswith('파'))
print(data.endswith('.'))

print("------------------")

data = "   파이썬은 아주 Easy!!! but High...   "

# 비파괴
print(data.strip())
print(data.lstrip())
print(data.rstrip())

print("------------------")


data2 = data.replace("파이썬은", "장고는")
print(data2)
print(data.split())
print(data.split('!!!'))
data2 = "정말인가요?"
print(data + data2)
print(data)
data3 = data + data2
print(data3)
print(data.join(data2))
print(data)


data4 = '-'
print(data4.join('1234'))

print('정말' in data2)
























