print("### 중국집 주문  ###")

jjang = 4500
bbong = 3000

print("짜장면 가격:", jjang,"원")
print("짬뽕 가격:", bbong, "원")
print("")

jjang_cnt = int(input("짜장면 주문 수: "))
bbong_cnt = int(input("짬뽕 주문 수: "))
print("")

jjang_price = jjang * jjang_cnt
bbong_price = bbong * bbong_cnt
total_price = jjang_price + bbong_price

print("짜장면 금액:", jjang_price,"원")
print("짬뽕 금액:", bbong_price,"원")
print("전체 주문 금액:", total_price,"원")