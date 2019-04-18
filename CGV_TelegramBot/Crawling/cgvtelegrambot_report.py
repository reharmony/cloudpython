# -*- coding: utf-8 -*- 

'''
Created on 2019. 4. 15.

@author: jeong
'''
import telepot
import os
import time
import threading


token= "836234072:AAEKFOj3hmfbhg-pY5ScDrbxPUiYCG39xe8"

mc = "-1001159590408"

bot = telepot.Bot(token)

status = True

bot.sendMessage(mc, "## 서버 정상 작동중 ##")

print("메세지 전송 완료")   




