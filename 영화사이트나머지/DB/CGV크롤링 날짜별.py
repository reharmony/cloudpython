import requests
import datetime
from datetime import timedelta
import os
from bs4 import BeautifulSoup  

# 오늘날짜 구하기
today = datetime.date.today()
today = today.strftime('%Y%m%d')

#     
# for i in range (0,20) :
#     day = today + timedelta(i)
#     day = day.strftime('%Y%m%d')
#     print(day)
 
# 순위 정보 받아올 주소에 오늘날짜 입력
response = requests.get('http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=%s&screencodes=&screenratingcode=&regioncode=' % today)
  
html = response.text

# BS 이용해서 원하는 값만 추출
soup = BeautifulSoup(html, 'html.parser') #html.parser를 사용해서 soup에 넣겠다
     
datelist=[]
for tag in soup.select('#slider > div > ul > li:nth-child(2) > div > a'):
    datelist.append(tag.text.strip())
print(datelist)
for i in datelist:
    print(i)
    
#     # 상영정보 있는지 확인하는 변수
#     count = 0
#      
#     # txt 파일 초기화
#     f_write=None
#     f_write = open("cgv.txt", "w")                            
#     f_write.write("")
#     f_write.close()
     

#     
#     # 아맥 개봉 영화 테이블 위치 찾기
#     for a in range (0,20):
#         for tag in soup.select('li:nth-child(%d) > div > div > div.info-hall > ul > li:nth-child(2) > span > span' % a):        
#             screen = tag.text.strip()
#             if screen == 'IMAX':
#                 # 제목 찾기
#                 for tag in soup.select('li:nth-child(%d)> div > div.info-movie > a > strong' % a):
#                     title = tag.text.strip()
#                     # txt파일에 제목 입력                
#                     f_write = open("cgv.txt", "w")                  
#                     f_write.write(title + day + "\n")
#                     f_write.close() 
#                     # 테이블 안에서 아맥관 순서 찾기
#                     for b in range(0,20):
#                         for tag in soup.select('li:nth-child(%d) > div > div:nth-child(%d) > div.info-hall > ul > li:nth-child(2) > span > span' % (a, b)):        
#                             screen = tag.text.strip()
#                             if screen == 'IMAX':
#                                 # 상영시간 및 잔여좌석 찾기
#                                 for tag in soup.select('li:nth-child(%d) > div > div:nth-child(%d) > div.info-timetable > ul > li > a' % (a, b)):
#                                     taglist= tag.text.strip()
#                                     showtime = taglist.replace("잔여좌석", "    잔여좌석: ")
#                                     # txt파일에 상영시간 및 잔여좌석  입력
#                                     f_write = open("cgv_%s.txt" % day, "a")
#                                     f_write.write(showtime + "\n")
#                                     f_write.close()                            
#                                     print(showtime) # 내용 확인용 출력
#             
#             if "IMAX" in screen :
#                 count += 1
#             else:
#                 pass
#             
#     if count >= 1:
#         print("상영정보있음")
#     else:
#         print("상영정보없음")
# 
# 
# # 상영정보 존재 여부
# # if exist == "yes":
# #     print("상영정보 O")
# # else:
# #     print("상영정보 X")
