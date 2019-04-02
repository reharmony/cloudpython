# 변수 정의
a = 1000
b = 1200
c = 800
drink = "a"
drink_sum = []
money_sum = 0
price_sum = 0


while True:

# 금액 투입
    money = int(input("투입할 금액을 입력해주세요>> "))
    money_sum = money_sum + money
    print("-----------------------------------------")
# 음료 선택
    while True: 
        drink = input("음료수를 선택해주세요(a,b,c)>> ")
        if drink == "a" or drink =="b" or drink =="c":
            drink_sum = drink_sum + drink 
            print("-----------------------------------------")
            break
        else:
            print("잘못된 입력값입니다. a,b,c중에서 다시 선택해주세요>> ")
            print("-----------------------------------------")

# 음료에 따른 가격 변수 입력
    if drink == "a":
        price = 1000        
    elif drink == "b":
        price = 1200  
    elif drink == "c":
        price = 800
    
    
# 투입금액과 상품가격 비교 후 잔돈 계산
    if money >= price:
        jan = money - price
    else :
        jan = money
        print("투입하신 금액이 부족합니다.")

# 종료 여부 묻기
    ending = input("선택을 종료하시겠습니까? (y/n)>> ")
    while True:        
        if ending == "y" and money >= price:
            print("-----------------------------------------")
            print("선택하신 음료 %c가 나왔습니다." % drink)
            print("잔돈 %d원을 반환합니다." % jan)
            break
        elif ending == "y" and money < price:
            print("-----------------------------------------")
            print("투입하신 금액 %d원을 다시 반환합니다." % jan)
            break
        elif ending == "n":
            break        
        else :
            print("-----------------------------------------")
            print("잘못된 값입니다. 다시 입력해주세요. (y/n)>> ")
    if ending == "y":
        break
    if ending == "n":
        pass
