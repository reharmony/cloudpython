### 변수로 분석 ###

# 1. 문자열 입력
data = input("문자열을 입력하세요>> ")

# 2. 변수 초기화
int_count = 0
str_count = 0
blank_count = 0

# 3. for으로 하나씩 판별
for i in range(0,len(data)):
    data2= data[i]
    # 숫자 카운트
    if data2.isdigit() == 1:
        int_count += 1
    # 문자 카운트
    elif data2.isalpha() == 1:
        str_count += 1
    # 공백 카운트
    elif data2.isspace() == 1:
        blank_count += 1

# 3. 형식별 개수 출력
print("숫자: %d개, 문자: %d개, 공백: %d개" 
      % (int_count,str_count,blank_count))
