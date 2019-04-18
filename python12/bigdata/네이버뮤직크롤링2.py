'''
Created on 2019. 4. 18.

@author: user
'''
import requests
from bs4 import BeautifulSoup

def get_title():# 코드로 입력받은 회사의 주가 크롤링
    
    url = "https://music.naver.com/home/index.nhn" # 크롤링할 주소
    result = requests.get(url) # 해당 url 내용 가져오기

    bs_obj = BeautifulSoup(result.content, "html.parser") # html을 인식해서 가져오기
    title_list=[]
    for rank in range(1,11):
        for tag in bs_obj.select('div.tc_panel.tc_selected > table > tbody > tr._tracklist_move._track_dsc.list%d > td.name > span > a' % rank):
            title_list.append(tag.text)

    return title_list
    
    
    

def get_singer():# 코드로 입력받은 회사의 주가 크롤링
  
    url = "https://music.naver.com/home/index.nhn" # 크롤링할 주소
    result = requests.get(url) # 해당 url 내용 가져오기

    bs_obj = BeautifulSoup(result.content, "html.parser") # html을 인식해서 가져오기
    singer_list=[]
    for tag in bs_obj.select('div.tc_panel.tc_selected > table > tbody > tr._tracklist_move._track_dsc.list1.on > td._artist.artist > span'):            
        singer_list.append(tag.text)
    
    for rank in range(2,11):
        for tag in bs_obj.select('div.tc_panel.tc_selected > table > tbody > tr._tracklist_move._track_dsc.list%d > td._artist.artist > span' % rank):            
            singer_list.append(tag.text)

    return singer_list
    

def total_info():
    title_list = get_title()
    singer_list = get_singer()

    print("순위\t노래명\t\t\t\t\t\t가수")
#     
    for index in range(0,10,1):
        rank = index+1
        title = title_list[index]
        singer = singer_list[index]
        print(rank, "\t", title, "\t\t\t\t\t\t", singer)

# def page_info():
#     
# #     for i in range(1,11):
#     global page
#     
#     
#     total_info(company_names, now_price_list)

total_info()