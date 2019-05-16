'''
Created on 2019. 4. 18.

@author: user
'''
import requests
from bs4 import BeautifulSoup

title=[]

def get_price(code):# 코드로 입력받은 회사의 주가 크롤링

    url = "https://finance.naver.com/item/main.nhn?code=" + code # 크롤링할 주소
    result = requests.get(url) # 해당 url 내용 가져오기
    # print(result)
    # print(result.content) # 그냥 한 줄로 쭐 가져오기
    bs_obj = BeautifulSoup(result.content, "html.parser") # html을 인식해서 가져오기
    # print(bs_obj)
       
    no_today = bs_obj.find("p", {"class":"no_today"}) # 특정 값 지정해서 가져오기
#     print(no_today)
    blind = no_today.find("span",{"class":"blind"})
    print(title)
    print(blind.text + "원")
    
get_price('027740')
    