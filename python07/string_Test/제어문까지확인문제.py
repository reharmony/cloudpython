'''
# 1. 두 수를 입력받아서 더 큰 수를 판별하는 프로그램
num1 = int(input("첫번째 숫자를 입력하세요.>>"))
num2 = int(input("두번째 숫자를 입력하세요.>>"))
if num1 > num2:
    print("첫번째 숫자가 더 큽니다.")
elif num1 < num2:
    print("두번째 숫자가 더 큽니다.")
else:
    print("두 수가 같습니다.")


# 2. 한 수를 입력받아서 짝수/홀수를 판별하는 프로그램
num3 = int(input("숫자를 입력하세요.>> "))
if num3 % 2 == 0:
    print("입력하신 숫자는 짝수입니다.")
else:
    print("입력하신 숫자는 홀수입니다.")


# 3. 이번달의 계절을 판별하는 프로그램 (3~5월 봄, 6~8 여름, 9~11 가을, 12~2 겨울)
import datetime
now = datetime.date.today()
month = now.month
if month == 3 or month == 4 or month == 5:
    print("이번달은 봄입니다.")
elif month == 6 or month == 7 or month == 8:
    print("이번달은 여름입니다.")
elif month == 9 or month == 10 or month == 11:
    print("이번달은 가을입니다.")
else:
    print("이번달은 겨울입니다.")


# 4. 6개의 값을 입력받아 그 중에서 제일 큰 수를 찾는 프로그램
number =[]
for i in range(0,6):
    number.append(int(input("%d번째 숫자를 입력하세요.>> " % (i+1)))) 

print(max(number))


# 5. 입력값(숫자1, 연산기호, 숫자2)를 받아서 사칙연산 프로그램 만들기
num01 = int(input("첫번째 숫자를 입력하세요.>> "))
symbol = input("연산기호를 입력하세요.(+,-,*,/)>>")
num02 = int(input("두번째 숫자를 입력하세요.>> "))

if symbol == "+":
    print("계산결과: %d %s %d =" % (num01, symbol, num02), num01 + num02)
elif symbol == "-":
    print("계산결과: %d %s %d =" % (num01, symbol, num02), num01 - num02)
elif symbol == "*":
    print("계산결과: %d %s %d =" % (num01, symbol, num02), num01 * num02)
elif symbol == "/":
    print("계산결과: %d %s %d =" % (num01, symbol, num02), num01 / num02)
 


# 6. 시작값과 끝나는 값을 입력받아 시작값~끝값을 전부 더하는 프로그램
first = int(input("시작값을 입력하세요.>> "))
last = int(input("끝값을 입력하세요.>> "))
sum=0
print("@ 전부 더한 결과: ", end="")
for i in range(first,last+1):
    sum = sum + i
    if i < last:
        print("%d + " % i, end="")
    else:
        print("%d = " % i, end="")
print(sum)


# 7. 두 개의 리스트(이름, 점수)를 사용하여 표를 출력
name = []
point = []

student = int(input("학생수를 입력하세요.>> "))

for i in range(0,student):
    name.append(input("%d번째 학생의 이름을 입력하세요>> " % (i+1)))
    point.append(int(input("%d번째 학생의 점수를 입력하세요>> " % (i+1))))

print("")
print("전체학생수: %d명" % student)
print("------------------------")

for i in range(0,student):
    print("%s: %d" % (name[i], point[i]))

print("------------------------")

totalpoint = 0

for i in range(0,student):
    totalpoint += point[i]

avg = totalpoint/student

print("평균: %d점" % avg)


# 8. 두 개의 딕셔너리(이름, 점수)를 사용하여 표를 출력

point_dic={"김아무개":100, "송아무개":85, "정아무개":90, "이아무개":70}

name_list=[]
name_list=list(point_dic.keys())
point_list=[]
point_list=list(point_dic.values())

print("")
print("전체학생수: %d명" % len(point_dic))
print("------------------------")

for i in range(0, len(name_list)):
    print("%s: " % name_list[i], end="")
    print(point_list[i])

print("------------------------")

totalpoint2 = 0

for i in range(0, len(point_list)):
    totalpoint2 += point_list[i]

avg2 = totalpoint2 / len(point_list)

print("평균 :  %d점" % avg2)


# 9. 영웅 세 명 입력받기
hero =[]

for i in range(0,3):
    hero.append(input("영웅을 입력하세요.>> "))
    if hero[i] == "종료":
        print("프로그램을 종료합니다.")
    
if hero.count("배트맨") >= 1:
    print("박쥐인간이군요!")
if hero.count("슈퍼맨") >= 1:
    print("하늘을 나눈군요!")
if hero.count("아이언맨") == 1:
    print("철의인간이군요!")



# 10. 영웅 6명을 입력받아 숫자 세기
hero2 =[]

for i in range(0,6):
    hero2.append(input("영웅을 입력하세요.(슈퍼맨, 배트맨, 아이언맨)>> "))
    if hero2[i] == "종료":
        print("프로그램을 종료합니다.")

print("배트맨: %d명, 슈퍼맨: %d명, 아이언맨: %d명" 
      % (hero2.count("배트맨"),hero2.count("슈퍼맨"),hero2.count("아이언맨")))

'''

























    
    
    
    
    
    