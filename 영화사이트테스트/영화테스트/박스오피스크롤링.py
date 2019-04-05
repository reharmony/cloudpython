import requests
import datetime

# 오늘날짜 구하기
now = datetime.datetime.now()
today = "%04d%02d%02d" % (now.year, now.month, now.day)
print(today)

# 순위 정보 받아올 주소에 오늘날짜 입력
response = requests.get('http://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cnt&date=%s' % today)
 
html = response.text

# BS 이용해서 원하는 값만 추출
from bs4 import BeautifulSoup    
soup = BeautifulSoup(html, 'html.parser') #html.parser를 사용해서 soup에 넣겠다
for tag in soup.select('div[class=tit3]'):
    print(tag.text.strip())
    