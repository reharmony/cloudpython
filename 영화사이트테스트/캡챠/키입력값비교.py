'''
Created on 2019. 4. 11.

@author: user
'''
# 네이버 캡차 Open API 예제 - 키 입력값 비교
import os
import sys
import urllib.request
client_id = "y2ojBn2tSStkUq1zVx51"
client_secret = "nKd9wpjDJZ"
code = "1"
key = "V5Qj0QyU7wWdWky6"
value = "YOUR_CAPTCHA_VALUE"
url = "https://openapi.naver.com/v1/captcha/nkey?code=" + code + "&key=" + key + "&value=" + value
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)