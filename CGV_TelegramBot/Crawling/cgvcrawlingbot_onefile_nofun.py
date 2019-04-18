#!/usr/bin/python
# -*- coding: utf-8 -*-


import requests
import datetime
import os
from bs4 import BeautifulSoup
import telepot
import time

token= "876221220:AAEQWx1k0dlZZR_Q9iUUx5Qlpwn3twxIjb8"

mc = "463263981"

bot = telepot.Bot(token)

InfoMsg = "안녕하세요 IMAX 상영시간 안내봇입니다."

status = True

bot.sendMessage(mc, "IMAX 예매시간표를 검색합니다.\n잠시만 기다려주세요...")


# 오늘날짜 구하기
now = datetime.datetime.now()
today = "%04d%02d%02d" % (now.year, now.month, now.day)

# 순위 정보 받아올 주소에 오늘날짜 입력
response = requests.get('http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=%s&screencodes=&screenratingcode=&regioncode=' % today)     
html = response.text

# BS 이용해서 원하는 값만 추출
soup = BeautifulSoup(html, 'html.parser') #html.parser를 사용해서 soup에 넣겠다    

# 상영정보 있는 날짜의 url만 추출
urllist=[]
day_list=[]
title_list=[]
time_str=""
time_list=[]
time_list_total=[]
all_list=[]
for tag in soup.select('#slider > div > ul > li > div > a'):
    urllist.append(tag.get('href')) 
for i in urllist:
    url = 'http://www.cgv.co.kr/common/showtimes' + i[0:63].replace('./i', '/i')
    day = url[91:99]
    print(day)
    
    response = requests.get(url) 
    html = response.text
    # BS 이용해서 원하는 값만 추출
    soup = BeautifulSoup(html, 'html.parser') #html.parser를 사용해서 soup에 넣겠다
    
    # 아맥 개봉 영화 테이블 위치 찾기
    for a in range (0,20):
        for tag in soup.select('li:nth-child(%d) > div > div > div.info-hall > ul > li:nth-child(2) > span > span' % a):        
            screen = tag.text.strip()
            if screen == 'IMAX':
                day_list.append(day)
                # 제목 찾기
                for tag in soup.select('li:nth-child(%d)> div > div.info-movie > a > strong' % a):
                    title = tag.text.strip()
                    title_list.append(title)
                    print(title)
                    # 테이블 안에서 아맥관 순서 찾기
                    for b in range(0,20):
                        for tag in soup.select('li:nth-child(%d) > div > div:nth-child(%d) > div.info-hall > ul > li:nth-child(2) > span > span' % (a, b)):        
                            screen = tag.text.strip()
                            if screen == 'IMAX':
                                # 상영시간 및 잔여좌석 찾기                                    
                                for tag in soup.select('li:nth-child(%d) > div > div:nth-child(%d) > div.info-timetable > ul > li > a' % (a, b)):                                      
                                    taglist= tag.text.strip()                                        
                                    showtime = taglist.replace(u"잔여좌석", u"    잔여좌석: ")
#                                         print(showtime + "showtime")
                                    time_str += "\n" + showtime
#                                         print(time_str + "time_str")
                                    time_list.append(time_str)
#                                         print(time_list)
                                time_list_total.append(time_list)
                                time_str=""
                                time_list=[]
                                print(time_list_total)                                     
#                                     print(time_str)                                                
#                                     print(time_list) # 내용 확인용 출력
    all_list.append(title + "    " + day + "\n")
    print()


title=""    
for x in range(len(time_list_total)):
    title = all_list[x]
    time_sum=""
    for y in range(len(time_list_total[x])):
        time_sum = time_list_total[x][y]  
    
    print(title + time_sum)    
    bot.sendMessage(mc, title + time_sum)
    time_sum=""

print("메세지 전송 완료")   
