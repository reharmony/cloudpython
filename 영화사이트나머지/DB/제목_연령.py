import requests
 
response = requests.get('https://movie.naver.com/movie/running/current.nhn?view=list&tab=normal&order=reserve')
 
html = response.text

from bs4 import BeautifulSoup    
soup = BeautifulSoup(html, 'html.parser') #html.parser를 사용해서 soup에 넣겠다


tag_list=[]
for tag in soup.select('dt[class="tit"]'):
    tag2 = tag.text.strip()
    tag_list.append(tag2)

tag_split=[]
title=[]
age=[]

for i in range(0,31):
    tag_split.append(tag_list[i].splitlines())    

print("----")
for i in range(0,31):
    title.append(tag_split[i][1])
for i in range(0,31):
    age.append(tag_split[i][0])   
print("----")

# 제목
print(title)

# 연령
print(age)





















    



