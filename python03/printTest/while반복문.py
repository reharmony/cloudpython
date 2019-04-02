# target= 200
# 숫자를 입력 : 150 
# 틀렸습니다.
# 숫자를 입력 : 200
# 맞았습니다.
# 종료합니다.

target = int(input("숫자를 입력하세요>> "))

while target != 200:
    print("틀렸습니다.")
    print("-----------------------")
    target = int(input("숫자를 다시 입력하세요 (0을 입력시 종료)>> "))
    if target == 0:
        break
    
if target != 0:
    print("맞았습니다.")
    print("-----------------------")
    print("프로그램을 종료합니다..")
else :
    print("-----------------------")
    print("프로그램을 종료합니다..")
    