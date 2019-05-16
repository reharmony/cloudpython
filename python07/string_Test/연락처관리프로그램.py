### 연락처 관리 프로그램 ###

print("### 연락처 관리 프로그램 ###")

friends =[]

while True:
    print("-----------------------")
    
    print("1. 친구 리스트 출력")
    print("2. 친구 추가")
    print("3. 친구 삭제")
    print("4. 이름 변경")
    print("9. 종료")
    
    menu = input("메뉴를 선택하시오: ")
            
    if menu == "1":
        print(friends)
    elif menu == "2":
        friends.append(input("이름을 입력하시오: "))
    elif menu == "3":
        friends.remove(input("이름을 입력하시오: "))
    elif menu == "4":  
        name = input("기존 이름을 입력하시오: ")
        name2 = input("새로운 이름을 입력하시오: ")
        index = friends.index(name)
        friends.remove(name)
        friends.insert(index,name2)
    elif menu == "9":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 메뉴입니다. 다시 선택하세요.")
        


    

