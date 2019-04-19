'''
Created on 2019. 4. 17.

@author: user
'''
from tkinter import *
from 영화사이트화면구성 import 메인화면
from string import ascii_uppercase
from 영화사이트화면구성.DB연결 import *
import datetime
from datetime import timedelta

today = datetime.date.today() - timedelta(1)
yesterday = today.strftime('%Y%m%d')

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
    w2.configure(bg="white")
    cancel = Button(w2, text="예매하기", fg ='white', bg='red',width = 10, height =1, font = ("굴림", 15),relief = 'groove', overrelief = 'solid',command=endCall2) # 취소 버튼 (메인으로 돌아감)
    cancel.place(x=1250, y=725)   
    cancel = Button(w2, text="취소", width = 5, height =1, font = ("굴림", 15),relief = 'groove', overrelief = 'solid',command=endCall2) # 취소 버튼 (메인으로 돌아감)
    cancel.place(x=1385, y=725)   
    
    # 프레임 목록
    frame_list=LabelFrame(w2, text="영화명", font=('굴림', 15), relief="solid", bd=2, width = 400, height=300)
    frame_list.place(x=50,y=50)
    frame_time=LabelFrame(w2, text="상영 시간",font=('굴림',15),relief="solid", bd=2, width = 600, height=650, padx=10, pady=10)
    frame_time.place(x=50,y=360)
    frame_people=LabelFrame(w2, text="관람 인원", font=('굴림',15), pady=10,relief="solid", bd=2, width = 407, height=330)
    frame_people.place(x=50,y=630)
    frame_seat=LabelFrame(w2, text="좌석 선택", font=('굴림',15),relief="solid", bd=2, width = 600, height=650, padx=20, pady=70)
    frame_seat.place(x=500,y=50)
    frame_selectinfo=LabelFrame(w2, text="선택한 예매 정보", font=('굴림',15),relief="solid", bd=2, width = 300, height=650)
    frame_selectinfo.place(x=1150,y=50)
    
    
    # 영화 목록 리스트박스

    listbox = Listbox(frame_list, selectmode='single', width = 31, height=10, font=("굴림",19), activestyle='none', fg='white',bg='#191d1f')   
    
    def select_title(record):               
   
        start = 0   # row를 증가시켜주는 변수
        
        for result in record: 
            listbox.insert(start, result[0])
            start += 1
   
        listbox.pack()              

    selectday = "20190416"        
    record = db_process_select(selectday)
    select_title(record)    
       
    def title_fun(event):
        w = event.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        print(value)
        select_title.config(text=value)

    listbox.bind("<<ListboxSelect>>",title_fun)
    
    
    # 관람인원 스핀박스
    select_people=Label(frame_people)
    select_people.pack()
    
    def people_fun():
        print(spinbox.get())
        select_people.config(text="%s 명" % spinbox.get())
        select_price.config(text="%d 원" % (int(spinbox.get())*9000))
        
    spinbox=Spinbox(frame_people, from_ = 0, to = 10, width=29, font=("굴림",19),command = people_fun)
    spinbox.pack()
        
        
        
    # 상영 시간 라디오 버튼
    def time_fun():
        print(var_time.get())
        select_time.config(text=var_time.get())
            
    
    
    var_time = StringVar()
             
    radio1=Radiobutton(frame_time, text="09:00",font=("굴림",19), value="09:00", variable=var_time, command=time_fun)
    radio1.grid(row=0, column=0, padx= 15, pady=15)
    radio2=Radiobutton(frame_time, text="10:35",font=("굴림",19), value="10:35", variable=var_time, command=time_fun)
    radio2.grid(row=0, column=1, padx= 15, pady=15)
    radio3=Radiobutton(frame_time, text="12:10",font=("굴림",19), value="12:10", variable=var_time, command=time_fun)
    radio3.grid(row=0, column=2, pady=15)
    radio4=Radiobutton(frame_time, text="14:35",font=("굴림",19), value="14:35", variable=var_time, command=time_fun)
    radio4.grid(row=1, column=0, padx= 15, pady=15)
    radio5=Radiobutton(frame_time, text="16:50",font=("굴림",19), value="16:50", variable=var_time, command=time_fun)
    radio5.grid(row=1, column=1, padx= 15, pady=15)
    radio6=Radiobutton(frame_time, text="18:25",font=("굴림",19), value="18:25", variable=var_time, command=time_fun)
    radio6.grid(row=1, column=2, padx= 15, pady=15)
    radio6=Radiobutton(frame_time, text="19:50",font=("굴림",19), value="19:50", variable=var_time, command=time_fun)
    radio6.grid(row=2, column=0, pady=15)
    radio6=Radiobutton(frame_time, text="21:30",font=("굴림",19), value="21:30", variable=var_time, command=time_fun)
    radio6.grid(row=2, column=1, padx= 15, pady=15)
    radio6=Radiobutton(frame_time, text="23:15",font=("굴림",19), value="23:15", variable=var_time, command=time_fun)
    radio6.grid(row=2, column=2, pady=15)
            
        
        
    # 좌석도 버튼
    alpha = list(ascii_uppercase)
    number = list(range(1,101))
    
    def seat_fun():
        print(seat_all[x][y].get())
    
    
    # alphabet
    seat_list=[]
    for x in range(0,5):
        for y in range(0,5):
            seat_list.append("%s%c%d" % ("seat_",alpha[x], number[y])) 
#     print(seat_list)

    
    def press():
        seat_all[x][y].config(relief='sunken', state='active')
#         print("눌렸음")
       
    x = 0
    seat_all=[]
    for y in range(0,5):
        row = 0    
        seat_row=[]
        for i in range(x,x+5):
            seat_row.append(seat_list[i])
            row += 1
        x += 5
        seat_all.append(seat_row)
       
    for x in range(0,5):
        for y in range(0,5):
            seat_all[x][y] = Button(frame_seat, text=seat_all[x][y][5:7], bd = 5, width = 7, height =3, font = ("굴림", 15),relief = 'raised', overrelief = 'solid', state='normal', activebackground='gray', command=seat_fun) # 좌석 버튼
            seat_all[x][y].grid(row=x, column=y,padx=10, pady=10)   
    
    
    
    # 선택 정보
    ## 포스터
    poster = PhotoImage(file = 'm13.png') # 변수에 이미지 저장
    select_img = Label(frame_selectinfo) # Label에 이미지변수 할당
    select_img.configure(image=poster)
    select_img.image = poster    
    select_img.place(x=50, y = 20)
    
    ## 영화제목
    Label_title = Label(frame_selectinfo, text="영화명:", font=("굴림", 12), fg="black", bg="white") # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
    Label_title.place(x=10, y=300)
    select_title = Label(frame_selectinfo, text="", font=("굴림", 12), fg="black", bg="white") # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
    select_title.place(x=100, y=300)
    
    ## 상영시간
    Label_time = Label(frame_selectinfo, text="상영시간:", font=("굴림", 12), fg="black", bg="white") # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
    Label_time.place(x=10, y=340)
    select_time = Label(frame_selectinfo, text="", font=("굴림", 12), fg="black", bg="white") # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
    select_time.place(x=100, y=340)
    
    ## 관람인원
    Label_people = Label(frame_selectinfo, text="인원:", font=("굴림", 12), fg="black", bg="white") # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
    Label_people.place(x=10, y=380)
    select_people = Label(frame_selectinfo, text="", font=("굴림", 12), fg="black", bg="white") # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
    select_people.place(x=100, y=380)
    
    ## 좌석
    Label_seat = Label(frame_selectinfo, text="좌석:", font=("굴림", 12), fg="black", bg="white") # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
    Label_seat.place(x=10, y=420)
    select_seat = Label(frame_selectinfo, text="", font=("굴림", 12), fg="black", bg="white") # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
    select_seat.place(x=100, y=420)
    
    ## 결제금액
    Label_price = Label(frame_selectinfo, text="결제금액:", font=("굴림", 12), fg="black", bg="white") # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
    Label_price.place(x=10, y=460)
    select_price = Label(frame_selectinfo, text="", font=("굴림", 12), fg="black", bg="white") # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
    select_price.place(x=100, y=460)
    
    w2.mainloop()
