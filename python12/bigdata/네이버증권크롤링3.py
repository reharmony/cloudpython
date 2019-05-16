'''
Created on 2019. 4. 18.

@author: user
'''
import requests
from bs4 import BeautifulSoup

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
#     print(blind.text + "원")
    return blind.text


company_codes = ["027740","020560", "005930", "002995", "007460", "001745", "068270", "298690", "136480", "044960"]    
company_names = ["마니커", "아시아니항공","삼성전자", "금호산업", "에이프로젠","SK네트웍스","셀트리온","에어부산","하림","이글벳"]

index=0

for code in company_codes:
    price = get_price(code)
    name = company_names[index]
    print(name,":", price + "원")
    index = index + 1