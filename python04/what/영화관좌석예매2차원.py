print("###### 영화관 좌석 예매 프로그램2 #####")

# 초기좌석
seat = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]] 
print("-----------------------------------------")
count = 0

while True:
    # 좌석번호와 예매여부 출력
    print("", end="\t")
    for i in range(0,len(seat)):        
        print("%d열" % (i+1), end = "\t")
    for x in range(0,len(seat)):
        print("")
        print("%d행" % (x+1), end ="\t")
        for y in range(0,len(seat)):
            print(seat[x][y], end ="\t")            
    print("")
    
    # 예매할 좌석 번호 입력
    while True:
        row = int(input("예매할 행을 입력하세요.(1~5) (0입력시 종료)>> "))
        col = int(input("예매할 열을 입력하세요.(1~5) (0입력시 종료)>> "))
        if seat[row-1][col-1] == 0:
            seat[row-1][col-1] = 1
            break
        elif row == 0 or col == 0:
            break
        else:
            print("이미 예매된 좌석입니다. 다른좌석을 선택해주세요.")
            print("-----------------------------------------")
    if row == 0 or col == 0:
        print("-----------------------------------------")
        print("예매 프로그램을 종료합니다.")
        break
    
    # 선택한 좌석 출력
    print("-----------------------------------------")
    
    count+=1
    print("", end="\t")
    for i in range(0,len(seat)):        
        print("%d열" % (i+1), end = "\t")
    for x in range(0,len(seat)):
        print("")
        print("%d행" % (x+1), end ="\t")
        for y in range(0,len(seat)):
            print(seat[x][y], end ="\t")            
    print("")
    
    print("[%d행 %d열] 좌석이 선택되었습니다." % (row,col))
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
        print("=========================================")
        pass
    else:
        print("-----------------------------------------")
        print("선택된 좌석은 모두 %d석입니다." % count)
        print("총 티켓값은 %d원입니다."  % (count*9000) )
        print("-----------------------------------------")
        print("예매 프로그램을 종료합니다.")
        break

    

