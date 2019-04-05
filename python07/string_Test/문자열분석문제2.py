### 리스트로 분석 ###

# 1. 문자열 입력
data = input("문자열을 입력하세요>> ")

# 2. 리스트 정의
count = [0,0,0] # 0숫자, 1문자, 2공백

# 3. for문으로 하나씩 판별
for i in data:
    # 숫자 카운트
    if i.isdigit():
        count[0] += 1
    # 문자 카운트
    elif i.isalpha():
        count[1] += 1
    # 공백 카운트
    elif i.isspace():
        count[2] += 1


# 4. 형식별 개수 출력
print("숫자: %d개, 문자: %d개, 공백: %d개" 
      % (count[0],count[1],count[2]))
