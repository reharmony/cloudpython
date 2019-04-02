# 좋아하는 색상 입력 1~3
def color():
    co = (input("좋아하는 색상을 입력하세요 (빨강:1, 노랑:2, 파랑:3)>> "))
    return co

# 입력받은 색상번호로 수업 분류
def sub(co):
    if co == "1":
        result = "파이썬 스터디반"
    elif co == "2":
        result = "장고 스터디반"
    elif co == "3":
        result = "웹구축 스터디반"
    else :
        result = "1~3중에서 선택해주세요."
    return result
 
# 출력
a = color()
print(sub(a))