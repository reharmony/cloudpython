import requests
from bs4 import BeautifulSoup



html = requests.get('https://www.naver.com/').content #네이버의 html 값 가져옴
soup = BeautifulSoup(html, 'html.parser') #soup 객체 생성-> html.parser
        
title_list = [] #title_list라는 리스트를 하나만든다.
#class라는 명칭은 파이썬에서 이미 사용중이므로 bs4에서 검색시엔 class_로 사용한다.
for realtime in soup.find(class_='ah_list').find_all('li'): #class가 ah_list로 시작하는것을 찾고 그중 li로 시작하는 class를 모두 찾는다.
    tg2 = realtime.find(class_='ah_k') #그중에서도 클래스가 ah_k로 시작하는것을 찾는다.
    title_list.append(tg2.text)

for i, t in enumerate(title_list,1): #title_list에 숫자를 매긴다. (1부터시작함.)
    print("{}{} {}".format(i,"위",t))


