### 첫글자를 대문자로 입력했을 경우 ###

# 문자열 입력 받기
full = input("문자열을 입력하세요>> ")

# 이니셜 저장할 변수 초기화
first=""

# for문으로 대문자만 추출
for i in full:
    if i.isupper():
        first+=i

# 출력
print(first)

        