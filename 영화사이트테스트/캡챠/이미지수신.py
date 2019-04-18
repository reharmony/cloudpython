'''
Created on 2019. 4. 11.

@author: user
'''
# 네이버 캡차 API 예제 - 이미지수신
import os
import sys
import urllib.request
client_id = "y2ojBn2tSStkUq1zVx51"
client_secret = "nKd9wpjDJZ"
key = "V5Qj0QyU7wWdWky6" # 캡차 Key 값
url = "https://openapi.naver.com/v1/captcha/ncaptcha.bin?key=" + key
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    print("캡차 이미지 저장")
    response_body = response.read()
    with open('captcha.jpg', 'wb') as f:
        f.write(response_body)
else:
    print("Error Code:" + rescode)