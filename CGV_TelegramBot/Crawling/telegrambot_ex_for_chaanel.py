# -*- coding: utf-8 -*-
'''
Created on 2019. 4. 13.

@author: jeong
'''
import telepot
import time

token= "836234072:AAEKFOj3hmfbhg-pY5ScDrbxPUiYCG39xe8"

mc = "-1001159590408"

bot = telepot.Bot(token)

InfoMsg = "# 용산 IMAX 예매정보 안내봇입니다. #\n검색하려면 'ㄱㄱ'를 입력하세요."

status = True

bot.sendMessage(mc, "안녕하세요 cgVot입니다")

while status == True:
    time.sleep(5) 
