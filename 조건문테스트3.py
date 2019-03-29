'''
num = int(input("정수를 입력하세요: "))

if num % 2 == 0:
    print("입력된 정수는 짝수입니다.")
else:
    print("입력된 정수는 홀수입니다.")

print("프로그램이 종료되었습니다.")
'''

print("### 짜장면 가격 계산 ###")

zzang = 4500
mem = 3

if mem >= 5:
    print("일행:", mem,"명")
    print("총 가격:", zzang * mem - 2000, "원 (2000원 할인 적용)")
else:
    print("일행:", mem,"명")
    print("총 가격:", zzang * mem, "원 (할인 미적용)")