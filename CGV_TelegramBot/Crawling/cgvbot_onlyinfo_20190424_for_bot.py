# -*- coding: utf-8 -*-

import requests
import datetime
import os
import io
from bs4 import BeautifulSoup  
import telepot
import time
import threading

# 목표날짜
target_day = "20190424"
target_day_bar = target_day[0:4] + "/" +  target_day[4:6] + "/" + target_day[6:8]
print(target_day_bar)

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
    day = i[55:63]
    day_list.append(day) 


showing=""

# 상영정보가 있으면 텔레그램으로 알림 메세지 전송
if target_day in day_list:
    
    token= "876221220:AAEQWx1k0dlZZR_Q9iUUx5Qlpwn3twxIjb8"

    mc = "463263981"
    
    bot = telepot.Bot(token)
    
#     InfoMsg = "용산 IMAX 어벤저스:엔드게임\n예매오픈 안내봇입니다."
    
    status = True
    
    bot.sendMessage(mc, target_day + "일의 예매가 열렸습니다!!!")
        
    for a in range (0,20):
        for tag in soup.select('li:nth-child(%d) > div > div > div.info-hall > ul > li:nth-child(2) > span > span' % a):        
            screen = tag.text.strip()
            if screen == 'IMAX':
                # 제목 찾기
                for tag in soup.select('li:nth-child(%d)> div > div.info-movie > a > strong' % a):
                    title = tag.text.strip()
                    # 테이블 안에서 아맥관 순서 찾기
                    for b in range(0,20):
                        for tag in soup.select('li:nth-child(%d) > div > div:nth-child(%d) > div.info-hall > ul > li:nth-child(2) > span > span' % (a, b)):        
                            screen = tag.text.strip()
                            if screen == 'IMAX':
                                # 상영시간 및 잔여좌석 찾기                                    
                                for tag in soup.select('li:nth-child(%d) > div > div:nth-child(%d) > div.info-timetable > ul > li > a' % (a, b)):                                      
                                    taglist= tag.text.strip()
                                    showtime = taglist.replace(u"잔여좌석", u"    잔여좌석: ")
                                    time_str += "\n" + showtime
                                all_info = title + "    " + target_day_bar + "\n" + time_str
                                bot.sendMessage(mc,all_info)
                            
           
    
    
    print("메세지 전송 완료")     
    
# 예매정보가 없으면 콘솔에만 수행내역 출력
else:
    print(target_day + "일의 예매정보가 없습니다.")
    pass


