'''
Created on 2019. 4. 17.

@author: user
'''
from tkinter import *
from 영화사이트화면구성 import 메인화면

w2 = None

def endCall2():
    global w2
    w2.destroy()
    메인화면.recall()
    
def call():
    global w2
    w2 = Tk()
    w2.geometry("1500x800+100+100") # 윈도우 크기 설정
    w2.title("예매 하기") # 윈도우 제목 설정
    w2.resizable(width=False, height=False) # 크기고정
#     w2.configure(bg="#FAF4C0")
    cancel = Button(w2, text="예매하기", fg ='white', bg='red',width = 10, height =1, font = ("굴림", 15),relief = 'groove', overrelief = 'solid',command=endCall2) # 취소 버튼 (메인으로 돌아감)
    cancel.place(x=1250, y=725)   
    cancel = Button(w2, text="취소", width = 5, height =1, font = ("굴림", 15),relief = 'groove', overrelief = 'solid',command=endCall2) # 취소 버튼 (메인으로 돌아감)
    cancel.place(x=1385, y=725)   
    
    # 프레임 목록
    frame_list=Frame(w2, relief="solid", bd=2, width = 400, height=300)
    frame_list.place(x=50,y=80)
    frame_select=Frame(w2, relief="solid", bd=2, width = 407, height=330)
    frame_select.place(x=50,y=370)
    frame_seat=Frame(w2, relief="solid", bd=2, width = 600, height=650)
    frame_seat.place(x=500,y=50)
    frame_selectinfo=Frame(w2, relief="solid", bd=2, width = 300, height=650)
    frame_selectinfo.place(x=1150,y=50)
    
    # 영화 목록 타이틀
    list_title = Label(w2, text="관람할 영화 선택", font=("굴림", 15)) # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
    list_title.place(x=50, y=50)
    
    # 영화 목록 리스트박스
    listbox = Listbox(frame_list, selectmode='single', width = 31, height=10, font=("굴림",19), activestyle='none')
    listbox.insert(0, "1번")
    listbox.insert(1, "2번")
    listbox.insert(2, "3번")
    listbox.insert(3, "4번")
    listbox.insert(4, "5번")
    listbox.insert(5, "6번")
    listbox.insert(6, "7번")
    listbox.insert(7, "8번")
    listbox.insert(8, "9번")
    listbox.insert(9, "10번")
    listbox.pack()

    
#     button1=Button(frame1, text="프레임1")
#     button1.place(x=10, y=10)
     
#     button2=tkinter.Button(frame2, text="프레임2")
#     button2.pack(side="left")
#     
    
    
    w2.mainloop()
