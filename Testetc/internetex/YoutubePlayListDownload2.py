from pytube import YouTube
from bs4 import BeautifulSoup
import requests
import sys
import json
import os
import time
 
workdir = os.path.dirname(os.path.realpath(__file__))
sys.stdout.write('url : ')
url = sys.stdin.readline().rstrip() #받고 싶은 playlist가 속의 클립 url을 입력받습니다.
headers = { 'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36' }
 
res = requests.get(url, headers=headers)
source = res.text #Response의 바디를 source라는 변수에 저장합니다. 이는 Raw Text 입니다.
 
soup = BeautifulSoup(source, 'html.parser') #BeautifulSoup로 Response 값을 분석합니다.
scripts = soup.find_all('script') # <script> 태그가 있는 부분만 찾아내어 Set으로 반환합니다.
 
found_i = -1
 
for (i, x) in enumerate(scripts):
    if 'window["ytInitialData"] = ' in str(x): #ytInitialData가 담긴 객체를 검색합니다.
        found_i = i
        break
 
if found_i < 0:
    print('Cannot find playlist') #만일 ytInitialData가 담긴 객체를 찾지 못했다면 그냥 종료합니다.
    exit()
 
raw_data = scripts[found_i].get_text()
str1 = raw_data.strip().split('window["ytInitialData"] = ')[1].split(';\n')[0]
 
#분석할 수 있도록 중간 부분만을 슬라이스해서 잘라옵니다.
 
j1 = json.loads(str1, encoding='utf8', strict=False) #String을 JSON Parsing하여 파이썬에서 사용할 수 있도록 해줍니다.
 
#이 때 strict를 false로 하지 않으면 인코딩 문제로 loads()가 제대로 실행되지 않을 수 있습니다.
 
toGet = []

print(j1)
#  
# for i in j1['contents']['twoColumnWatchNextResults']['playlist']['playlist']['contents']:
#     if 'unplayableText' not in i['playlistPanelVideoRenderer']: #비공개된 동영상일 경우엔 videoId가 나오지 않고 unPlayableText가 표시됩니다.
#         toGet.append(i['playlistPanelVideoRenderer']['videoId'])
#  
# for i in toGet:
#     getStr = 'https://www.youtube.com/watch?v=' + i
#     yt = YouTube(getStr)
#     file_name = yt.title
#     print('Downloading %s %s' % (file_name, time.time()))
#     yt.streams.filter(progressive=True, file_extension='mp4', only_audio=False).order_by('resolution').desc().first().download()