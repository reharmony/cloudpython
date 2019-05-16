### 딕셔너리로 분석 ###

# 1. 문자열 입력
data = input("문자열을 입력하세요>> ")

# 2. 딕셔너리 초기화
count = {"number":0,"alpha":0,"space":0}

# 4. for문으로 하나씩 판별
for i in data:
    # 숫자 카운트
    if i.isdigit():
        count["number"] += 1
    # 문자 카운트
    elif i.isalpha():
        count["alpha"] += 1
    # 공백 카운트
    elif i.isspace():
        count["space"] += 1


# . 형식별 개수 출력
print("숫자: %d개, 문자: %d개, 공백: %d개" % 
      (count["number"],count["alpha"],count["space"]))
