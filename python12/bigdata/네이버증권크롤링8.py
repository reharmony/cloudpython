import requests

from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import platform # 플랫폼(운영체제)에 맞는 폰트 체크
from matplotlib import font_manager, rc # matplot에서 한글 깨질 때 사용




def get_names(page):
    url = "https://finance.naver.com/sise/entryJongmok.nhn?&page="+str(page)
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    
    td_list = bs_obj.findAll("td", {"class":"ctg"})
#     print(td_list)
    company_names = []
    
    for td in td_list:
        company_names.append(td.find("a").text)
    
#     print(company_names)
    
    return company_names    

def get_now_price(page):
    url = "https://finance.naver.com/sise/entryJongmok.nhn?&page="+str(page)
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    
    td_list = bs_obj.findAll("td", {"class":"number_2"})
#     print(td_list)
    
    now_price_list = []
    
    td_list_count = len(td_list)
    
    for index in range(0, td_list_count, 4):
        now_price_list.append(td_list[index].text)
    
#     print(now_price_list)
    
    return now_price_list

def total_info():
    company_names = get_names()
    now_price_list = get_now_price()
    
    print("회사이름", "\t", "주식가")
    for index in range(0, 10, 1):
        name = company_names[index]
        price = now_price_list[index]
        print(name, "\t", price)
        
def total_info2(page):
    company_names = get_names(page)
    now_price_list = get_now_price(page)
    
    print(page, ":페이지>> 회사이름", "\t", "주식가")
    for index in range(0, 10, 1):
        name = company_names[index]
        price = now_price_list[index]
        print(name, "\t\t", price)
        
def total_info3(page):
    company_names = get_names(page)
    now_price_list = get_now_price(page)
    
    return company_names, now_price_list

# 페이지마다 별도 파일로 출력
def total_info4(page):
    company_names = get_names(page)
    now_price_list = get_now_price(page)
    
    file = open(str(page) + ".txt", "w")
    for index in range(0,10):
        name = company_names[index]
        price = now_price_list[index]
        file.write(name + "\t" + price + "\n")

# 전체 페이지 입력
# for page in range(1,11):
#     total_info4(page)

        
# 항목별로 나눠서 출력
# file2 = open("1.txt","r")
# for line in range(0,10):
#     line = file2.readline()
#     contents = line.split("\t")
#     print(contents[0]) # 회사이름
#     print(contents[1]) # 회사주가
    
        
file2 = open("1.txt","r")
for line in range(0,10):
    line = file2.readline()
    contents = line.split("\t")
    print(contents[0]) # 회사이름
    print(int(contents[1].replace(",","")))# 회사주가
        
file2 = open("1.txt","r")
name_list=[]
price_list=[]

for line in range(0,10):
    line = file2.readline()
    contents = line.split("\t")
    name_list.append(contents[0]) # 회사이름    
    price_list.append(int(contents[1].replace(",",""))) # 회사주가
    
print(name_list)
print(price_list)

# pandas 테이블로 만들기
# 데이터 프렐임을 만들어줌. 빅데이터 분석에 관한 여러가지 기능.
df = pd.DataFrame({"회사이름":name_list, "주식가":price_list})
print(df)
        
# numpy 이용 최대값, 최소값 등등 구하기
# 여러 수학적 기능들
print("최고가", np.max(df['주식가']))
print("자세한 정리", df.describe())

# 그래프

 # 한글 깨질 때 사용
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~') 


## 점으로 표시하기
# plt.figure(figsize=(10,6)) # 창 속성 지정 (크기 등)
# plt.grid() # 격자 삽입
# plt.xlabel('회사이름') # X축
# plt.ylabel('주가') # Y축
# plt.scatter(df['회사이름'],df['주식가'], s=50) # 각 항목을 표에 점으로 표시, s=숫자 -> 점의 크기

## 막대그래프로 표시하기
plt.figure(figsize=(10,6)) # 창 속성 지정 (크기 등)
plt.grid() # 격자 삽입
plt.xlabel('회사이름') # X축
plt.ylabel('주가') # Y축
df['주식가'].sort_values().plot(kind='barh', grid=True, figsize=(10,10))
plt.show() # tkinter의 mainloop 같은 기능





