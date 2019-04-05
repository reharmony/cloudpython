seat = [[0,0,0,0,0,0,0,0],
        [0,0," "," "," "," ",0,0],
        [0,0,0," "," ",0,0,0]]

while True:
    print("   ", end="")
    for i in range(1,9):
        print(i, end="  ")
    
    print("\n-------------------------")
    
       
    for x in range(0,len(seat)):  
        print(x+1, end="  ")     
        for y in range(0,len(seat[0])):
            print(seat[x][y], end="  ")    
        print()
    print("-------------------------")
    
    select = input("예매는 1, 종료는 0을 입력하세요.>> ")
    if select == "0":
        print("예매를 종료합니다.")
        break
    else:
        data1 = int(input("앉고 싶은 좌석을 입력하세요.(행)>> "))
        data2 = int(input("앉고 싶은 좌석을 입력하세요.(열)>> "))
        print("-------------------------")
        
        if seat[data1][data2] == 1:
            print("이미 예약이 완료된 자리입니다.")
            print("다른 좌석을 선택해주세요.")
        else:
            seat[data1][data2] = 1
            print("예매가 완료되었습니다.")
            print("=========================")
        
