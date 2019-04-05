import requests
 
response = requests.get('https://movie.naver.com/movie/running/current.nhn?view=list&tab=normal&order=reserve')
 
html = response.text

from bs4 import BeautifulSoup    
soup = BeautifulSoup(html, 'html.parser') #html.parser를 사용해서 soup에 넣겠다


tag_list=[]
for tag in soup.select('span[class="num"]'):
    tag2 = tag
    tag_list.append(tag2)

print(tag.list)
tag_split=[]
title=[]
age=[]




















    



