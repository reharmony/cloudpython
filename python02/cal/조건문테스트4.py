s = 1000
b = 2500

print("### 교보문고 구매상품 계산 ###")

s_cnt=int(input("스티커 구매 개수:"))
b_cnt=int(input("책갈피 구매 개수:"))

vip = int(input("vip: 1, 일반회원: 2 >>> "))

result = int((s*s_cnt + b*b_cnt))

if vip == 1:
    result = result * 0.9
else:
    result = result

print("스티커를 %d개 구매하고 책갈피를 %d개 구매하였습니다." % (s_cnt, b_cnt))
print("우수회원 10%% 할인을 적용하여 총 지불금액은 %d원 입니다." % result)
