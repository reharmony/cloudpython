import requests
 
response = requests.get('https://movie.naver.com/movie/running/current.nhn?view=list&tab=normal&order=reserve')
 
html = response.text

from bs4 import BeautifulSoup    
soup = BeautifulSoup(html, 'html.parser') #html.parser를 사용해서 soup에 넣겠다
body = soup.body

genreList=[]
for i in range(1,31):
    taged = soup.select('li:nth-child(%d) > dl > dd:nth-child(3) > dl > dd:nth-child(2) > span.link_txt > a' % i)   
    genreList.append([taged.text.strip() for taged in taged])

# 장르
print(genreList)
