print("###### 영화관 좌석 예매 프로그램 #####")

# 초기좌석
seat = [0] * 10
print("-----------------------------------------")

while True:
    # 좌석번호와 예매여부 출력
    print("[", end=" ")
    for i in range(0,len(seat)):    
        print(i+1, end=" ")
    print("]", end=" ")
    print("")
    
    print("[", end=" ")
    for i in range(0,len(seat)):    
        print(seat[i], end=" ")
    print(" ]", end=" ")
    print("")
    
    # 예매할 좌석 번호 입력
    while True:
        index = int(input("예매할 좌석 번호를 입력하세요.(1~10) (0입력시 종료)>> "))
        if seat[index-1] == 0:
            seat[index-1] = index
            break
        elif index == 0:
            break
        else:
            print("이미 예매된 좌석입니다. 다른좌석을 선택해주세요.")
            print("-----------------------------------------")
    if index == 0:
        print("-----------------------------------------")
        print("선택된 좌석은 모두 %d석입니다." % (10-seat.count(0)))
        print("총 티켓값은 %d원입니다."  % ((10-seat.count(0))*9000) )
        print("-----------------------------------------")
        print("예매 프로그램을 종료합니다.")
        break
    
    # 선택한 좌석 출력
    print("-----------------------------------------")
    
    print("[", end=" ")
    for i in range(0,len(seat)):    
        print(seat[i], end=" ")
    print(" ]", end=" ")
    print("")
    
    print("%d번 좌석이 선택되었습니다." % index)
    print("-----------------------------------------")
    
    # 반복 여부 묻기
    while True:
        ending = input("예매를 계속 하시겠습니까?(y/n)>> ")
        if ending == "y" or ending == "n":
            break
        else :
            print("잘못된 입력입니다.")
            print("-----------------------------------------")
            pass
    
    # 반복 또는 프로그램 종료
    if ending =="y":
        pass
    else:
        print("-----------------------------------------")
        print("선택된 좌석은 모두 %d석입니다." % (10-seat.count(0)))
        print("총 티켓값은 %d원입니다."  % ((10-seat.count(0))*9000) )
        print("-----------------------------------------")
        print("예매 프로그램을 종료합니다.")
        break

    

