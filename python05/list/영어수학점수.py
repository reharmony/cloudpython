# 점수 입력
eng=[]
math=[]
for i in range(0,3):
    data = int(input("%d번 학생의 영어점수를 입력하세요>> " % (i+1)))
    eng.append(data)
    data = int(input("%d번 학생의 수학점수를 입력하세요>> " % (i+1)))
    math.append(data)    

print("-----------------------------------------------")

# 입력받은 점수 출력

## 설명
print("3명의 학생의 각 영어, 수학 점수입니다.")
print()

## 학생 번호
for i in range(1,4):
    print("\t%d번" % i, end="")
print()

## 영어 점수
print("영어:\t", end="")
for i in range(0,3):
    print(eng[i],end="\t")
print()

## 수학 점수
print("수학:\t", end="")
for i in range(0,3):
    print(math[i],end="\t")
print()

print("-----------------------------------------------")

# 과목별 점수 합산
sum_eng = 0
sum_math = 0
for i in range(0,3):
    sum_eng = sum_eng + eng[i]
    sum_math = sum_math + math[i]
       
# 평균 점수 출력
print("영어 점수 평균은 %d점 입니다." % (sum_eng/3))
print("수학 점수 평균은 %d점 입니다." % (sum_math/3))

    

