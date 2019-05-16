seat = [[1,2,3],[4,5,6,7]]

# 행 수
print(len(seat))

print("----------------------------")

# 열 수
print(len(seat[0])) # 첫번째 행의 열 개수
print(len(seat[1])) # 두번째 행의 열 개수

print("----------------------------")

# 열 수2
seat2 = [[1,2,3,4],[5,6],[7,8,9]]
print(len(seat2[0]))
print(len(seat2[1]))
print(len(seat2[2]))

print("----------------------------")

# 열 수3
for i in range(0,3):
    print(len(seat2[i]))

print("----------------------------")

# 행열 수가 불규칙한 리스트 전체 출력
for x in range(0,len(seat2)): # 행을 출력해주는 반복문
    for y in range(0,len(seat2[x])): # 열을 출력해주는 반복문
        print(seat2[x][y], end=" ")
    print()
        
print(seat[0].count(1))

print("----------------")

seat3=[[1,2,3],[1,1,3],[1,1,1,1]]

for i in range(0,3):
    print(seat3[i].count(1))    
    print(seat3.count(1))
    print("------")
    
  
    
    
    
    