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
    
    InfoMsg = "안녕하세요 IMAX 상영시간 안내봇입니다."
    
    status = True
    
    bot.sendMessage(mc, target_day + "일의 예매가 열렸습니다!!!")   
    
    print("메세지 전송 완료")     
    
# 예매정보가 없으면 콘솔에만 수행내역 출력
else:
    print(target_day + "일의 예매정보가 없습니다.")
    pass
        
#     timer = threading.Timer(600, send)
#     timer.start()

