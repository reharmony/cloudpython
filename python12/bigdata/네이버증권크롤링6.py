'''
Created on 2019. 4. 18.

@author: user
'''
import requests
from bs4 import BeautifulSoup

def get_names(page):# 코드로 입력받은 회사의 주가 크롤링
    
    url = "https://finance.naver.com/sise/entryJongmok.nhn?&page=" + str(page) # 크롤링할 주소
    result = requests.get(url) # 해당 url 내용 가져오기
    # print(result)
    # print(result.content) # 그냥 한 줄로 쭐 가져오기
    bs_obj = BeautifulSoup(result.content, "html.parser") # html을 인식해서 가져오기
    # print(bs_obj)
#                
# # td_list = bs_obj.findAll("td", {"class":"ctg"}) # 특정 값 지정해서 가져오기
#     print(td_list)

    td_list = bs_obj.findAll("td", {"class":"ctg"}) # 특정 값 지정해서 가져오기
    
    
#     print(td_list[0].find("a").text) # 단일 항목 추출
    company_names = []
    for td in td_list:
        company_names.append(td.find("a").text) # 여러 항목 추출
    
#     print(company_names)
        
    return company_names

def get_now_price(page):
    
    url = "https://finance.naver.com/sise/entryJongmok.nhn?&page=" + str(page) # 크롤링할 주소
    result = requests.get(url) # 해당 url 내용 가져오기
   
    bs_obj = BeautifulSoup(result.content, "html.parser") # html을 인식해서 가져오기
   
    td_list = bs_obj.findAll("td", {"class":"number_2"}) # 특정 값 지정해서 가져오기
    now_price_list = []
    
    td_list_count = len(td_list)
    
    for index in range(0,td_list_count, 4):
        now_price_list.append(td_list[index].text)
#     
#     for td in td_list:
#         now_price_list.append(td.text) # 여러 항목 추출
#         price = now_price_list
#         print(price)
    
        
#     print(now_price_list)
    
    return now_price_list



def total_info(page):
    
    company_names = get_names(page)
    now_price_list = get_now_price(page)
    print("회사이름", "\t    ", "주식가\t", page, "페이지")
    
    for index in range(0,10,1):
        name = company_names[index]
        price = now_price_list[index]
        print(name,": ", price)

# def page_info():
#     
# #     for i in range(1,11):
#     global page
#     
#     
#     total_info(company_names, now_price_list)

total_info(5)