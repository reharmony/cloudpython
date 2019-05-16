seat=["○","○","○","○","○","○","○","○"]
Number=[]
total=0
while True:
    answer = input("좌석을 예약하시겠습니까?")
    if answer == "YES" or answer == "yes":
        i = 1
        print("영화 가격: 9000원")
        card = int(input("할인카드가 있으면 1, 없으면 0을 입력하세요"))
        print("예약할 인원수를 입력하세요")
        person= int(input(""))
        while  (i <= person):
            print(i,"번째 좌석을 선택하세요(1-8번)")
            print("현재좌석:",seat)
            select=int(input())
            if select >=1 and select <=8:
                if seat[select-1]=="●":
                    print("이미 예약된 좌석이니, 다른 좌석을 선택하세요")
                else:
                    seat[select-1]="●"
                    print(select,"번 좌석이 예약되었습니다")
                    print("현재좌석:", seat,"\n")
                    Number.append(select)
                    i += 1
                    if card:
                        total += 9000*0.9
                    else:
                        total += 9000
            else:
                print("1-8번 좌석 중 선택하세요!!")
        print("예약한 좌석", Number)
        print("총 금액:", int(total))
    elif answer == "NO" or answer =="no":
        print("예약을 취소합니다.")
        break
    else:
        print("다시 입력하세요")
        continue
