### 대소문자 구분없이 입력했을 경우 ###

# 문자열 입력받기
full = input("문자열을 입력하세요>> ")

# 이니셜 저장할 변수 정의 (첫번째 글자는 바로 저장)
first=full[0]

# for문으로 공백 다음에 오는 글자 추출
for i in range(0,len(full)):
    if full[i].isspace():
        first += full[i+1]        
        
# 대문자로 변경하여 출력
print(first.upper())

