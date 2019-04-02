# 소지금액 입력
def money():
    global total
    total = int(input("소지금액을 입력하세요>> "))
    print("현재 소지금액은 %d원입니다." % total)
    return total

# 1000원
def mf_1000():
    mo_1000 = total / 1000
    global re_1000 
    re_1000 = total % 1000   
    print("# 1000원 지폐는 %d개입니다." % mo_1000)
    return re_1000
        
# 500원
def mf_500():
    mo_500 = re_1000 / 500
    global re_500
    re_500 = re_1000 % 500
    print("# 500원 동전은 %d개입니다." % mo_500)
    return re_500

# 100원
def mf_100():
    mo_100 = re_500 / 100
    global re_100
    re_100 = re_500 % 100
    print("# 100원 동전은 %d개입니다." % mo_100)
    return re_100

# 10원
def mf_10():
    mo_10 = re_100 / 10
    global re_10
    re_10 = re_100 % 10
    print("# 10원 동전은 %d개입니다." % mo_10)
    return re_10

# 1원
def mf_1():
    mo_1 = re_10 / 1
    print("# 1원 동전은 %d개입니다." % mo_1)
    

a = money()
b = mf_1000()    
c = mf_500()
d = mf_100()
e = mf_10()
f = mf_1()    
    
    
