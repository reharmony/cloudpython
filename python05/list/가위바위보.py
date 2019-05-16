import random

print("### 가위바위보 게임 프로그램 ###")
while True:
    # 사용자 패 입력
    while True:        
        you = input("가위,바위,보 중 하나를 입력하세요.>> ")
        if you == "가위" or you == "바위" or you == "보":
            break
        else:
            print("잘못 입력되었습니다.")
            print("----------------")
    
    # 컴퓨터 패 설정
    rand = random.randrange(0,3)
    com = ["가위","바위", "보"]
    
    # choice 함수 사용법
    # random 대신 
    # choice = ["가위", "바위", "보"]
    # random.choice(choice)
    # 형식도 사용가능
    
    
    # 고른 패 보여주기
    print("당신:", you)
    print("컴퓨터:", com[rand])
    
    # 내가 가위 냈을 경우
    if you == "가위":
        if com[rand] == "가위":
            print("무승부입니다.")
        elif com[rand] == "바위":
            print("컴퓨터의 승리입니다.")
        else:
            print("당신의 승리입니다.")
            
    # 내가 바위 냈을 경우
    elif you == "바위":
        if com[rand] == "가위":
            print("당신의 승리입니다.")
        elif com[rand] == "바위":
            print("무승부입니다.")
        else:
            print("컴퓨터의 승리입니다.")
            
    # 내가 보 냈을 경우
    elif you == "보":
        if com[rand] == "가위":
            print("컴퓨터의 승리입니다.")
        elif com[rand] == "바위":
            print("당신의 승리입니다.")
        else:
            print("무승부입니다.")
    
    print("---------------------------")
    
    # 계속 도전할지 묻기
    while True:  
        ending = input("계속하시겠습니까?(예/아니오)>> ")
        if ending == "예" or ending == "아니오":
            break
        else:
            print("잘못 입력되었습니다.")
            print("------------------------------")
    if ending  == "예":
        print("------------------------------")
        print("### 가위바위보 게임 프로그램 ###")
        pass
    else:
        print("### 프로그램을 종료합니다. ###")
        break












