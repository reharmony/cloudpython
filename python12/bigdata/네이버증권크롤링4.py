'''
Created on 2019. 4. 18.

@author: user
'''
import requests
from bs4 import BeautifulSoup

title=[]

def get_price():# 코드로 입력받은 회사의 주가 크롤링

    url = "https://finance.naver.com/sise/" # 크롤링할 주소
    result = requests.get(url) # 해당 url 내용 가져오기
    # print(result)
    # print(result.content) # 그냥 한 줄로 쭐 가져오기
    bs_obj = BeautifulSoup(result.content, "html.parser") # html을 인식해서 가져오기
    # print(bs_obj)
  
    for tag in bs_obj.select('#popularItemList > li > a'): # 1~10위 회사명 한 번에 불러오기 
        title.append(tag.text) 
        
    print(title)
    
get_price()
    