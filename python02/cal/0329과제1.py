
# 1번 문제
print("--------------------------------")
degree = input("오늘의 기온은? ")
grade = input("오늘 나의 평가는? ")
size = input("나의 신발 사이즈는? ")
print("--------------------------------")
print("오늘은 %s도, 나의 평가는 %s, 신발 사이즈는 %s입니다." % (degree, grade, size))
print("")

# 2번 문제
a = int(input("첫번째 숫자를 입력하세요: "))
b = int(input("두번째 숫자를 입력하세요: "))

if a == b:
    print("두 수가 같습니다.")
else:
    print("두 수가 다릅니다.")
    
print("")


# 3번 문제
given = int(input("받은 돈: "))
price = int(input("상품의 총액: "))
vat = int(price * 0.1)
remain = int(given - price)

print("")

print("### 영수증 ###")
print("받은돈:", given)
print("상품의 총액:", price)
print("부가세:", vat)
print("잔돈:", remain)


# 4번 문제
key = 4000
mouse = 3000

print("키보드 가격:", key)
key_cnt = int(input("키보드 구매 개수: "))
print("마우스 가격:", mouse)
mouse_cnt = int(input("마우스 구매 개수: "))

print("-------------------------------")

key_price = key * key_cnt
mouse_price = mouse * mouse_cnt
total = key_price + mouse_price

print("키보드 총 가격:", key_price)
print("마우스 총 가격:", mouse_price)
print("제품 총 가격:", total)




# 5번 문제
name = input("이름을 입력하세요: ")
age = input("나이를 입력하세요: ")
dept = input("소속을 입력하세요: ")

print("----------------------------")

print("당신의 이름은:", name)
print("당신의 나이는:", age)
print("당신의 소속은:", dept)

