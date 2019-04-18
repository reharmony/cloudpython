# -*- coding: utf-8 -*-

import requests
import datetime
import os
import io
from bs4 import BeautifulSoup  
import telepot
import time
import threading

day=['20190424','20190425','20190426']

# 목표날짜
for i in range(0,3):
    target_day = day[i]
    
    url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=%s' % target_day 
    response = requests.get(url) 
    html = response.text
    # BS 이용해서 원하는 값만 추출
    soup = BeautifulSoup(html, 'html.parser') #html.parser를 사용해서 soup에 넣겠다
    
    showing=""
    time_str=""
    
    token= "836234072:AAEKFOj3hmfbhg-pY5ScDrbxPUiYCG39xe8"
    
    mc = "-1001159590408"
    
    bot = telepot.Bot(token)
     
    status = True    
    
    # 아맥 상영중인 영화의 테이블 위치 찾기
    for a in range (0,20):
        for tag in soup.select('li:nth-child(%d) > div > div > div.info-hall > ul > li:nth-child(2) > span > span' % a):                  
            screen = tag.text.strip()
            if screen == 'IMAX':
                # 테이블 안에서 아맥관 순서 찾기
                for b in range(0,20):
                    for tag in soup.select('li:nth-child(%d) > div > div:nth-child(%d) > div.info-hall > ul > li:nth-child(2) > span > span' % (a, b)):        
                        screen = tag.text.strip()
                        if screen == 'IMAX':
                            time_str=""
                            # 상영시간 및 잔여좌석 찾기                                                                
                            for tag in soup.select('li:nth-child(%d) > div > div:nth-child(%d) > div.info-timetable > ul > li > a' % (a,b)):                            
                                taglist= tag.text.strip()
                                showtime = taglist.replace(u"잔여좌석", " ")
                                time_str += "\n" + showtime
                            if time_str == "":
                                pass
                            else:
                                all_info = target_day[6:8] + time_str                  
#                                 print(all_info)
                                bot.sendMessage(mc,all_info)
#                                 print("메세지 전송 완료")     



    

