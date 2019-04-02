# 기능추가1) 너무커요/작아요
# 기능추가2) target 값을 랜덤으로 지정
# 기능추가3) 몇 번만에 맞추었을까? (반복횟수 구하기)

import random

target = random.randrange(1,101)
count = 0
while True:
    data = int(input("숫자를 입력하세요 (1~100입력, 0입력시 강제종료)>> "))
    # 정답일 경우
    if data == target:        
        print("정답입니다.")
        count += 1
        print("당신이 시도한 횟수는 %d번입니다." % count)
        print("---------------------")
        print("프로그램을 종료합니다.")
        break
    # 타겟보다 클 경우
    elif data > target:
        print("너무 커요")
    # 강제종료        
    elif data == 0:
        print("---------------------")
        print("프로그램을 강제종료합니다.")
        break
    # 타겟보다 작을 경우
    else:
        print("너무 작아요")       
    # 카운트 증가 
    count += 1
    print("당신이 시도한 횟수는 %d번입니다." % count)
    print("---------------------")
    