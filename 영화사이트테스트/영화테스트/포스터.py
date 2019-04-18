import requests
 
response = requests.get('https://movie.naver.com/movie/running/current.nhn?view=list&tab=normal&order=reserve')
 
html = response.text

from bs4 import BeautifulSoup    
soup = BeautifulSoup(html, 'html.parser') #html.parser를 사용해서 soup에 넣겠다
body = soup.body

posterList=[]
for i in range(1,31):
    taged = soup.select('li:nth-child(%d) > div > a > img' % i)   
    posterList.append([taged.get('src').replace('99_141','203_290') for taged in taged]) # 다른 페이지의 더 큰 이미지로 주소 변경
    
# 포스터 주소
# print(posterList)

print(posterList[0])

