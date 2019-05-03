from tkinter import *
import threading
import time
import random

# 스레드 클래스
class Thread:
    car = None
    thread = None

    def __init__(self, w,img,x1,y1):
        # 이미지 할당
        self.car = Label(w)
        icon = PhotoImage(file = img)
        self.car.configure(image = icon)
        self.car.image = icon
        # 스레드 설정
        self.thread = threading.Thread(target = self.run, args=(self.car,x1,y1))
        self.thread.start()

    # 스레드 실행 함수
    def run(self, car,x1,y1):
        speed = 0
        while True:
            speed = random.randrange(10,50) # 한 번에 10~50 사이로 움직임
            if x1 >= 500: # 골인 지점
                break
            x1 = x1 + speed
            self.car.place(x=x1,y=y1)
            time.sleep(0.5) # 대기시간



# 자동차 배치
def Cars():
    # 창, 파일명, x좌표, y좌표
    car1 = Thread(w,'carimage1.png',10,70)
    car2 = Thread(w,'carimage2.png',10,180)
    car3 = Thread(w,'carimage3.png',10,300)

# 메인코드
if __name__ == '__main__':
    # 윈도우 배치
    w = Tk()
    w.title('자동자 경주')
    w.geometry('500x400')

    # 버튼 배치
    startbutton = Button(w,text='경기 시작', command=Cars)
    startbutton.pack(side=TOP, fill=X, ipadx=3, ipady=3,padx=5, pady=5)

    w.mainloop()
