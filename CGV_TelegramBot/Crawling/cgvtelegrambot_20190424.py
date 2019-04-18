# -*- coding: utf-8 -*- 

'''
Created on 2019. 4. 13.

@author: jeong
'''
import telepot
from cgvcrawling_20190424 import txt_export
import os
import io
import time
import threading


token= "876221220:AAEQWx1k0dlZZR_Q9iUUx5Qlpwn3twxIjb8"

mc = "463263981"

bot = telepot.Bot(token)

InfoMsg = "안녕하세요 IMAX 상영시간 안내봇입니다."

status = True

# bot.sendMessage(mc, "예매시간표를 검색합니다.")

def send():
    
    bot.sendMessage(mc, "예매시간표를 검색합니다.")

    f_open = None
    str_open = ""
    
    day = txt_export() 
    
    f_open = io.open("cgv_%s.txt" % day, "r", encoding = "utf-8")                            
    str_open = f_open.read()
    print(str_open)
    f_open.close()  
 
    bot.sendMessage(mc, str_open)
 
    print("메세지 전송 완료")   
#     
#     timer = threading.Timer(600, send)
#     timer.start()


if __name__ == '__main__':
    if txt_export() == "no":
        print("해당일의 상영 정보가 없습니다.")        
    else:                    
        send()
       


