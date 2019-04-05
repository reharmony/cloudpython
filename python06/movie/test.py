import requests 
response = requests.get('http://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cnt&date=20190404')
html = response.text
from bs4 import BeautifulSoup    
soup = BeautifulSoup(html, 'html.parser') 
soup.select('div[class=tit3]')