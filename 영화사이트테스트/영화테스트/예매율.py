import requests
 
response = requests.get('https://movie.naver.com/movie/running/current.nhn?view=list&tab=normal&order=reserve')
 
html = response.text

from bs4 import BeautifulSoup    
soup = BeautifulSoup(html, 'html.parser') #html.parser를 사용해서 soup에 넣겠다

# 연령제한
for tag in soup.select('dl[class="lst_dsc"]'):
    print(tag.text.strip())

tag2 = tag.text.strip()
print(tag2)

c_lst = [x for x in tag2 if x]
print(c_lst)

