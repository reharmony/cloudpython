# ★★★★★★★★★★ 3줄 출력하기
for y in range(0,3):
    for x in range(0,10,1):
        print("★", end="")
    print()

print("----------------------------------")

# 다이아 반쪽    
for y in range(0,10):   
    for x in range(0,y):
        print("★", end="")
    print()

for z in range(10,0,-1):   
    for x in range(0,z):
        print("★", end="")
    print()
 
print("---------------------------------")

# 다이아 테스트
for t in range(9,0,-2):
    for s in range(0,t,2):
        print(" ", end="")
    for x in range(t,10,2):
        print("★", end="")
    print()
            
print("---------------------------------")            

# 다이아 만들기
for x in range(0,10,1):
    print("  " * (10-x), end="")
    print("★ " * x)
for x in range(10,0,-1):
    print("  " * (10-x), end="")
    print("★ " * x)
            
print("---------------------------------")    
        
# while 문으로 구현
x = 0
while x <= 10:
    print("★" * x)
    x = x+1