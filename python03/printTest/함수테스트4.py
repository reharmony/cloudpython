# if __name__ == '__main__':
    
# 숫자 입력 받기
number = int(input("금액을 입력>> "))



# 1000원짜리 개수 구하기
c1000 = number // 1000 # "//" 는 정수 몫 구하는 연산자
print("1000원 짜리 개수", c1000, "장")

# 1000원으로 나눈 나머지 금액 구하기
money = number % 1000
print("나머지 금액: ", money, "원")
print("------------------")
    
    
    
# 500원짜리 개수 구하기
c500 = number // 500
print("500원 짜리 개수", c500, "개")

# 500원으로 나눈 나머지 금액 구하기
money = number % 500
print("나머지 금액: ", money, "원")
print("------------------")
    
    
    
# 100원짜리 개수 구하기
c100 = number // 100
print("100원 짜리 개수", c100, "개")

# 100원으로 나눈 나머지 금액 구하기
money = number % 100
print("나머지 금액: ", money, "원")
print("------------------")



# 50원짜리 개수 구하기
c50 = number // 50
print("50원 짜리 개수", c50, "개")

# 50원으로 나눈 나머지 금액 구하기
money = number % 50
print("나머지 금액: ", money, "원")
print("------------------")



# 10원짜리 개수 구하기
c10 = number // 10
print("10원 짜리 개수", c10, "개")

# 10원으로 나눈 나머지 금액 구하기
money = number % 10
print("나머지 금액: ", money, "원")
print("------------------")


