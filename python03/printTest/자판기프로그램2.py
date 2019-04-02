# 변수 정의
a = 1000
b = 1200
c = 800
drink = "a"


while True:

# 금액 투입
    money = int(input("투입할 금액을 입력해주세요>> "))  
    print("-----------------------------------------")
# 음료 선택
    while True: 
        drink = input("음료수를 선택해주세요(a,b,c)>> ")
        if drink == "a" or drink =="b" or drink =="c":
            print("-----------------------------------------")
            break
        else:
            print("잘못된 입력값입니다. a,b,c중에서 다시 선택해주세요")
            print("-----------------------------------------")

# 음료에 따른 가격 변수 입력
    if drink == "a":
        price = 1000        
    elif drink == "b":
        price = 1200  
    else :
        price = 800
    
    
# 투입금액과 상품가격 비교 후 잔돈 계산
    if money >= price:
        jan = money - price        
        print("선택하신 음료 %c가 나왔습니다." % drink)
        print("잔돈 %d원을 반환합니다." % jan)        
    else :
        jan = money
        print("투입하신 금액이 부족합니다.")
        print("투입하신 금액 %d원을 다시 반환합니다." % jan)

# 종료 여부 묻기
    print("-----------------------------------------")
    ending = input("음료수를 더 구매하시겠습니까? (y/n)>> ")
    while True:        
        if ending == "n" :            
            break       
        elif ending == "y":
            print("-----------------------------------------")
            break        
        else :
            print("-----------------------------------------")
            print("잘못된 값입니다. 다시 입력해주세요. (y/n)>> ")
    if ending == "n":
        print("-----------------------------------------")
        print("프로그램을 종료합니다.")
        break        
    if ending == "y":
        pass
