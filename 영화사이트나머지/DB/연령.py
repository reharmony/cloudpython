import requests
 
response = requests.get('https://movie.naver.com/movie/running/current.nhn?view=list&tab=normal&order=reserve')
 
html = response.text

from bs4 import BeautifulSoup    
soup = BeautifulSoup(html, 'html.parser') #html.parser를 사용해서 soup에 넣겠다
body = soup.body

tag2=[]
for tag in soup.select('dt > span'):
    tag2.append(tag.text.strip())

star=[]   
for i in range(0,31):
    star.append(tag2[i])

# 연령
print(star)




