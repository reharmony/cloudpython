user = "root" # 변수명은 대문자로 쓰지 않는다.
pw = "1234"

iId = input("id: ")
iPw = input("pw: ")

if iId == user:
    print("올바른 id입니다.")
else:
    print("잘못된 id입니다.")
    
if iPw == pw:
    print("올바른 pw입니다.")
else:
    print("잘못된 pw입니다.")
    
if iId == user and iPw == pw:
    print("로그인에 성공했습니다.")
else:
    print("로그인에 실패했습니다.")