# 인원, 가격을 입력을 받아서,
# 두 수를 곱한 후,
# 곱한 수가 10000원이 넘으면, 2000원 할인 해줄 예정이다.

def money():
    person = int(input("인원을 입력하세요: "))
    price = int(input("가격을 입력하세요: "))
    total = person * price
    if total >= 10000 :
        return total - 2000
    else :
        return total
    

a = money()
print("총 가격은 %d원입니다." % a)