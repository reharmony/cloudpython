'''
Created on 2019. 4. 18.

@author: user
'''
import requests
from bs4 import BeautifulSoup

def get_title(page):# 코드로 입력받은 회사의 주가 크롤링
    
    url = "https://music.naver.com/listen/top100.nhn?domain=TOTAL&duration=1d&page=" + str(page) # 크롤링할 주소
    result = requests.get(url) # 해당 url 내용 가져오기

    bs_obj = BeautifulSoup(result.content, "html.parser") # html을 인식해서 가져오기

    td_list = bs_obj.findAll("td", {"class":"name"}) # 특정 값 지정해서 가져오기

    title_list=[]
    for i in range(1,51):
        print(td_list[i].text.strip())
        title_list.append(td_list[i].text.strip())

    return title_list

def singer_names(page):# 코드로 입력받은 회사의 주가 크롤링
    
    url = "https://music.naver.com/listen/top100.nhn?domain=TOTAL&duration=1d&page=" + str(page) # 크롤링할 주소
    result = requests.get(url) # 해당 url 내용 가져오기

    bs_obj = BeautifulSoup(result.content, "html.parser") # html을 인식해서 가져오기

    td_list = bs_obj.findAll("td", {"class":"_artist artist"}) # 특정 값 지정해서 가져오기
    td_list2 = bs_obj.findAll("td", {"class":"_artist artist no_ell2"}) # 특정 값 지정해서 가져오기
    singer_list=[]
    for i in range(len(td_list)):
        print(td_list[i].text.strip())
        singer_list.append(td_list[i].text.strip())
    for i in range(len(td_list2)):
        print(td_list2[i].text.strip())
        singer_list.append(td_list2[i].text.strip())

    return singer_list


def test(page):
    url = "https://music.naver.com/listen/top100.nhn?domain=TOTAL&duration=1d&page=" + str(page) # 크롤링할 주소
    result = requests.get(url) # 해당 url 내용 가져오기

    bs_obj = BeautifulSoup(result.content, "html.parser") # html을 인식해서 가져오기

#     td_list = bs_obj.findAll("tr", {"class":"_tracklist_move data1"}) # 특정 값 지정해서 가져오기
#     td_list2 = bs_obj.findAll("td", {"class":"_artist artist no_ell2"}) # 특정 값 지정해서 가져오기
    td_list = bs_obj.findAll("tr", {"class":"_tracklist_move data1"}) # 특정 값 지정해서 가져오기
    singer_list=[]
    if "_artist artist no_ell2" in td_list:
        td_list2 = td_list.findAll("td", {"class":"_artist artist no_ell2"})
        print(td_list2)
        print("있음")
    else:
        print("없음")
        singer_list = bs_obj.findAll("td", {"class":"_artist artist"}) # 특정 값 지정해서 가져오기
    for i in range(len(singer_list)):
        print(singer_list[i].text.strip())
        
    
#     print(singer_list[0].text.strip())
        
        
#     td_list2 = td_list.findAll("td", {"class":"_artist artist no_ell2"}) # 특정 값 지정해서 가져오기
#     print(td_list)
    
#     if td_list2 !="":
#         print("true")
#         for i in range(len(td_list2)):
#             print(td_list2[i].text.strip())
#             singer_list.append(td_list2[i].text.strip())
#         print(td_list2[1].text.strip())
#     else:
#         print("false")
     
#     print(td_list2[1].text.strip())
    
#     for i in range(len(td_list)):
#         print(td_list[i].text.strip())
#         singer_list.append(td_list[i].text.strip())
#     for i in range(len(td_list2)):
#         print(td_list2[i].text.strip())
#         singer_list.append(td_list2[i].text.strip())

    return singer_list


def total_info():
    pass
#     company_names = get_names()
# #     now_price_list = get_now_price()
#     print("회사이름", "\t    ", "주식가\t")
#     
#     for index in range(0,10,1):
#         name = company_names[index]
# #         price = now_price_list[index]
#         print(name,": ")

# def page_info():
#     
# #     for i in range(1,11):
#     global page
#     
#     
#     total_info(company_names, now_price_list)

test(1)
# singer_names(1)