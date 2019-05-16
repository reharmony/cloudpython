### 문자열 처리 프로그램 ###

print("### 강아지 목록 ###")

dogs=""
while True:
    dog = input("강아지의 이름을 입력하시오.(0입력시 종료)>> ")
    if dog == "0":
        break
    else:
        dogs += (dog + ",")
        
print("강아지들의 이름: ", dogs)
    
    
    
    

