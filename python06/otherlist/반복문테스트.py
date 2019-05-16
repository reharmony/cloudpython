data1 = ["감자", "고구마", "양파"]

for x in range(0,3):
    print(data1[x])

for y in data1:
    print(y)
    
print()

data2 = "나는 파이썬 프로그래머"
for z in data2:
    print(z)
    
print()

# 거꾸로 돌리기 + 그걸 리스트에 넣기
size = len(data2)
reverse =[]
for z in range(size-1,-1,-1):
    print(z, ":",data2[z])
    reverse.append(data2[z])

print("")

print(reverse)

print("")

for r in range(0,len(reverse)):
    print(reverse[r], end="")

print("\n")

singer = {6:"송아무개", 4:"김아무개",8:"정아무개"}
data3 = singer.keys()
print(data3)

for j in data3:
    print(singer[j])

print()
for j in singer.keys():
    print(singer[j])
    
# 딕셔너리에 있는 값을 in으로 검색할 때는 키 값을 검색한다.
print(1 in singer)
print(6 in singer)
print("송아무개" in singer)
