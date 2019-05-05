'''
Created on 2019. 5. 6.

@author: jeong
'''
from tkinter import *
from tkinter.ttk import *
import tkinter
import threading
import time
import random

# 프로그래스바 생성 클래스
class Progress:
    progress = None
    thread = None
    

    # 프로그래스바 생성자
    def __init__(self, w, color):
        # 프로그래스바 색상 설정
        s = Style()
        s.theme_use('clam')
        s.configure("%s.Horizontal.TProgressbar" % color, troughcolor ='black', background=color) # 바 배경색 / 바 색
        # 프로그래스바 배치
        self.progress = Progressbar(w, style="%s.Horizontal.TProgressbar" % color, orient = HORIZONTAL, length = 500)
        self.progress.pack(side=TOP, fill = X, ipadx = 10, ipady = 10, padx=10, pady=10)
        # 스레드 설정
        self.thread = threading.Thread(target = self.progressArmy, args=(self.progress,))
        self.thread.start()

    # 프로그래스바 값 변경 함수
    def progressArmy(self, progress):
        vacation = 0 # 휴가 일수
        while True:
            vacation = random.randrange(0,10) # 한 번에 0~10 사이로 휴가 부여
            if progress['value'] >= 100: # 군생활 진행도 (최대값 100)
                break
            progress['value'] = progress['value'] + vacation
            time.sleep(0.5) # 대기 시간

# 프로그래스바 배치
def gotoArmy():
    # 군인 3명 (윈도우 명, 프로그래스바 색상)
    army3 = Progress(w, 'blue')
    army2 = Progress(w, 'yellow')
    army1 = Progress(w, 'red')

# 메인 코드
if __name__ == '__main__':
    # 윈도우 배치
    w = Tk()
    w.title('군생활 진행도 (휴가가 많으면 체감시간 빨라짐)')
    w.geometry('500x250')

    # 입대 버튼
    armybutton = tkinter.Button(w,text='입대', font=('굴림',15, 'bold'),relief = 'ridge',fg = 'white', bg = '#2F9D27', command = gotoArmy)
    armybutton.pack(side = TOP, fill = X, ipadx = 5, ipady = 5, padx=10, pady=10)

    w.mainloop()