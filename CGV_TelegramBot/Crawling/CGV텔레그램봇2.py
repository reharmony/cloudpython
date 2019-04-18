'''
Created on 2019. 4. 13.

@author: jeong
'''
import telepot
from CGV크롤링_상영날짜자동판별 import txt_export
import os
import time
import threading


token= "876221220:AAEQWx1k0dlZZR_Q9iUUx5Qlpwn3twxIjb8"

mc = "463263981"

bot = telepot.Bot(token)

InfoMsg = "안녕하세요 IMAX 상영시간 안내봇입니다."

status = True


def handle(msg):
    content, chat, id = telepot.glance(msg)
    print(content, chat, id)
    
    if content == "text":
        if msg['text'] == "ㄱㄱ":
            bot.sendMessage(id, "예매시간표를 검색합니다.")
            send()
        else:
            bot.sendMessage(id, InfoMsg)

def send():
    f_open = None
    str_open = ""
    
    day_list = txt_export() 
    
    for day in day_list:
        f_open = open("cgv_%s.txt" % day, "r")                            
        str_open = f_open.read()
        print(str_open)
        f_open.close()  
    
        bot.sendMessage(mc, str_open)

    print("메세지 전송 완료")   

  
 
bot.message_loop(handle)
 
while status == True:
    time.sleep(5)        
 
# timer = threading.Timer(60)
# timer.start()


    



