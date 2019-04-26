import requests
 
response = requests.get('https://movie.naver.com/movie/running/current.nhn?view=list&tab=normal&order=reserve')
 
html = response.text

from bs4 import BeautifulSoup    
soup = BeautifulSoup(html, 'html.parser') #html.parser를 사용해서 soup에 넣겠다
body = soup.body

tag_list=[]
for tag in soup.select('dl > dd:nth-child(3) > dl > dd:nth-child(2)'):
    tag2 = tag.text.strip()
    tag_list.append(tag2)

tag3=[]
for i in range(0,31):
    tag3.append(tag_list[i].split())

tag4=[]
for i in range(0,31):
    tag4.append(tag3[i][len(tag3[i])-4])

# 상영시간
print(tag4)
