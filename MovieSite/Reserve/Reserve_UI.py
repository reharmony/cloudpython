# -*- coding: utf-8 -*-
'''
Created on 2019. 4. 17.

@author: user
'''
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image
from Main import Main_UI
from string import ascii_uppercase
from CommonDB.DB_select_boxoffice import *
import datetime
from datetime import timedelta
from functools import partial
from Reserve.DB_insert_reserve_info import * 
from Reserve.DB_select_reserve_seat import * 
from CommonDB.DB_select_poster import * 
from CommonDB.image_url_down_onefile import *

# 기준날짜 설정
today = datetime.date.today() - timedelta(1)
yesterday = today.strftime('%Y%m%d')


member ="0"
w2 = None

# 예매화면 닫고 메인화면 불러오기
def endCall2():
    global w2
    w2.destroy()
    Main_UI.recall()

# 예매화면    
def call():
    global w2
    w2 = Tk()
    w2.geometry("1500x800+170+130") # 윈도우 크기 설정
    w2.title("예매 하기") # 윈도우 제목 설정
    w2.resizable(width=False, height=False) # 크기고정
    w2.configure(bg="#FFFF8F")
    
    # 예매 선택 정보 저장하는 리스트
    reserve_info=[0,0,0,0,yesterday, member]
    
    # 예약 좌석
    reserved=[]
   
    # 이미 예매된 좌석인지 체크
    def seat_check_fun(): 
        title = reserve_info[0]    
        time = reserve_info[2]        
        reserved=[]
        if title != 0 and time != 0:
            reserved_seat = db_process_select_reserve(title, time, yesterday)
            print(reserved_seat)
            for seat in reserved_seat:
                print(seat[0])
                reserved.append(seat[0])
            print(reserved)
            for x in range(0,5):
                for y in range(0,5):
                    if seat_all[x][y]['text'] not in select_seat_list:
                        if seat_all[x][y]['text'] not in reserved:
                            seat_all[x][y].config(state='normal', relief='raised', fg='black', bg="#FFCD50") 
                        else:
                            seat_all[x][y].config(state = 'disabled', relief = 'sunken', bg = 'gray', disabledforeground='#C9C9C9')
        else:
            pass
      

    # 예매 버튼 동작
    def reserve():
        if len(select_seat_list) != int(spinbox.get()):
            messagebox.showwarning("예매 오류", "선택된 관람인원과 좌석수가 일치하지 않습니다.")
        elif label_select_title['text'] == "":
            messagebox.showwarning("예매 오류", "관람하실 영화를 선택해 주세요.")
        elif label_select_time['text'] == "":
            messagebox.showwarning("예매 오류", "상영시간을 선택해 주세요.")
        else:
            if messagebox.askyesno("예매 확인", "선택한 정보로 결제하시겠습니까?"):
                print("결제완료")
                print(reserve_info)
                title = reserve_info[0]
                time = str(reserve_info[2])
                people = str(reserve_info[1])
                seat_list = reserve_info[3]
                seat_total=""
                for seat in seat_list:
                    seat_total += seat + " "
                db_process_insert(title, time, people, seat_list, seat_total, selectday)
                endCall2()                
            else:
                print("취소")
  
    # 예매하기 버튼 
    button_reserve = Button(w2, text="예매하기", fg ='white', bg='red',width = 10, height =1, font = ("굴림", 15),relief = 'groove', overrelief = 'solid',command=reserve) # 예매 버튼
    button_reserve.place(x=1250, y=725)
    
    # 취소 버튼   
    button_cancel = Button(w2, text="취소", width = 5, height =1, font = ("굴림", 15),relief = 'groove', overrelief = 'solid',command=endCall2) # 취소 버튼 (메인으로 돌아감)
    button_cancel.place(x=1385, y=725)   
    
    
    
    # 프레임 목록
    
    ## 리스트박스 프레임
    frame_list=LabelFrame(w2, text="영화명", font=('굴림', 15, "bold"), bg= "#FFFF8F", fg="black", relief="groove", bd=10, width = 400, height=300, pady=5)
    frame_list.place(x=50,y=50)
    
    ## 상영시간 프레임
    frame_time=LabelFrame(w2, text="상영 시간",font=('굴림',15, "bold"), bg="#FFFF8F",  fg="black", relief="groove", bd=10, width = 650, height=400, padx=15, pady=10)
    frame_time.place(x=50,y=380)
    
    ## 관람인원 프레임
    frame_people=LabelFrame(w2, text="관람 인원", font=('굴림',15, "bold"), bg="#FFFF8F",  fg="black", pady=10,relief="groove", bd=10, width = 407, height=330)
    frame_people.place(x=50,y=623)
    
    ## 좌석도 프레임
    frame_seat=LabelFrame(w2, text="좌석 선택", font=('굴림',15, "bold"),bg="#FFFF8F",  fg="black", relief="groove", bd=10, width = 600, height=650, padx=30, pady=60)
    frame_seat.place(x=511,y=50)
    
    ## 선택한 예매 정보 프레임
    frame_selectinfo=LabelFrame(w2, text="선택한 예매 정보", font=('굴림',15, "bold"), bg="#FFFF8F",  fg="black", relief="groove", bd=10, width = 300, height=650)
    frame_selectinfo.place(x=1150,y=50)
    
    
    
    
    
    
    
    
    # 영화 목록 리스트박스
    
    ## 리스트박스 배치 및 속성 설정
    listbox = Listbox(frame_list, selectmode='single', width = 31, height=10, font=("굴림",19), fg='black',bg='#F6DD61', bd=3, relief='groove')   
    
    ## 리스트박스 내용 (영화제목) 할당
    def select_title(record):    
        start = 0   # row를 증가시켜주는 변수
        for result in record: 
            listbox.insert(start, result[0]) # row값, 표시할 내용
            start += 1
        listbox.pack()              
    
    # 기준날짜 설정
    selectday = yesterday
    # 기준날짜의 DB 받아오기        
    record = db_process_select(selectday)
    # 리스트박스 내용(영화제목) 보내주기
    select_title(record)    
    ## 리스트박스 내용(영화제목) 선택시 이벤트   
    def title_fun(event):
        w4 = event.widget
        index = int(w4.curselection()[0])
        title = w4.get(index)
        print(title)
        label_select_title.config(text=title)
        reserve_info[0] = title
        poster_url = db_process_select_poster(title)
        poster_name= poster_down_resize(poster_url)
        print(poster_name)        
#         select_img.configure(file=poster_url[49:])
        poster2 = ImageTk.PhotoImage(file = u'D:\jjh\python\pyworkspace\MovieSite\Poster\%s.jpg' % poster_name)
#         poster2 = ImageTk.PhotoImage(file = 'D:\\Users\\jeong\\Documents\\workspacePython\\MovieSite\\Poster\\%s.jpg' % poster_name)
        select_img.configure(image=poster2)        
        select_img.image = poster2
        seat_check_fun()

    ## 리스트박스 내용 선택시 호출할 함수  
    listbox.bind("<<ListboxSelect>>",title_fun)
    
    
    
    
    
    
    
    
    
    
    # 관람인원 스핀박스
    
    ## 인원수를 선택된 좌석보다 낮게 내릴시 동작하는 함수
    def seat_over_fun():
        messagebox.showwarning("예매 오류", "관람인원이 선택된 좌석수보다 적습니다.")
   
    ## 스핀박스 값 변경시 이벤트 
    def people_fun():
        print(spinbox.get())
        label_select_people.config(text="%s 명" % spinbox.get())
        label_select_price.config(text="%d 원" % (int(spinbox.get())*9000))
        reserve_info[1] = int(spinbox.get()) 
        if len(select_seat_list) < int(spinbox.get()):
            seat_check_fun()
        elif len(select_seat_list) == int(spinbox.get()):
            for x in range(0,5):
                for y in range(0,5):
                    if seat_all[x][y]['text'] not in select_seat_list:
                        seat_all[x][y].config(state='disable')
        else:
            seat_over_fun()
#                     
    ## 스핀박스 배치 및 속성 설정
    spinbox=Spinbox(frame_people, from_ = 0, to = 5, width=29, font=("굴림",19),command=people_fun,  fg="black", bg="#F6DD61", relief='groove')
    spinbox.pack()
        
    
    
    
        
        
        
        
        
    # 상영 시간 라디오 버튼
    
    ## 라디오 버튼 클릭시 이벤트
    def time_fun():
        print(var_time.get())
        label_select_time.config(text=var_time.get())
        reserve_info[2] = var_time.get()
        seat_check_fun()
        
    
    ## 라디오 버튼 누를시 얻는 값    
    var_time = StringVar()
    
    ## 라디오 버튼 배치 및 속성 설정
    radio1=Radiobutton(frame_time, text="09:00",font=("굴림",19), bg="#FFFF8F", fg="black", value="09:00", variable=var_time, command=time_fun)
    radio1.grid(row=0, column=0, padx= 15, pady=10)
    radio2=Radiobutton(frame_time, text="10:35",font=("굴림",19), bg="#FFFF8F", fg="black", value="10:35", variable=var_time, command=time_fun)
    radio2.grid(row=0, column=1, padx= 15, pady=10)
    radio3=Radiobutton(frame_time, text="12:10",font=("굴림",19), bg="#FFFF8F", fg="black", value="12:10", variable=var_time, command=time_fun)
    radio3.grid(row=0, column=2, pady=10)
    radio4=Radiobutton(frame_time, text="14:35",font=("굴림",19), bg="#FFFF8F", fg="black", value="14:35", variable=var_time, command=time_fun)
    radio4.grid(row=1, column=0, padx= 15, pady=10)
    radio5=Radiobutton(frame_time, text="16:50",font=("굴림",19), bg="#FFFF8F", fg="black", value="16:50", variable=var_time, command=time_fun)
    radio5.grid(row=1, column=1, padx= 15, pady=10)
    radio6=Radiobutton(frame_time, text="18:25",font=("굴림",19), bg="#FFFF8F", fg="black", value="18:25", variable=var_time, command=time_fun)
    radio6.grid(row=1, column=2, padx= 15, pady=10)
    radio6=Radiobutton(frame_time, text="19:50",font=("굴림",19), bg="#FFFF8F", fg="black", value="19:50", variable=var_time, command=time_fun)
    radio6.grid(row=2, column=0, pady=10)
    radio6=Radiobutton(frame_time, text="21:30",font=("굴림",19), bg="#FFFF8F", fg="black", value="21:30", variable=var_time, command=time_fun)
    radio6.grid(row=2, column=1, padx= 15, pady=10)
    radio6=Radiobutton(frame_time, text="23:15",font=("굴림",19), bg="#FFFF8F", fg="black", value="23:15", variable=var_time, command=time_fun)
    radio6.grid(row=2, column=2, pady=10)
            
            
            
            
            
            
            
            
            
            
            
    # 좌석도 버튼
    
    ## 알파벳과 숫자 리스트
    alpha = list(ascii_uppercase)
    number = list(range(1,101))
    
    select_seat_list=[]
#   
    ## 좌석 버튼 클릭시 이벤트  
    def seat_fun(x,y):
        select_seat_str=''   
        if seat_all[x][y]['relief'] == 'raised':
            seat_all[x][y].config(relief='sunken', bg = '#FFD8D8') 
            print(seat_all[x][y]['text'])
            select_seat_list.append(seat_all[x][y]['text'])
            reserve_info[3] = select_seat_list
            print(select_seat_list)
            for seat in select_seat_list:
                select_seat_str += "%s  " % seat
            label_select_seat.config(text=select_seat_str)            
            if len(select_seat_list) >= int(spinbox.get()):
                for x in range(0,5):
                    for y in range(0,5):
                        if seat_all[x][y]['relief'] == 'raised':
                            seat_all[x][y].config(state='disabled')
             
        elif seat_all[x][y]['relief'] == 'sunken':
            seat_all[x][y].config(relief='raised', bg='#FFCD50')
            select_seat_list.remove(seat_all[x][y]['text'])            
            print(select_seat_list)
            for seat in select_seat_list:
                select_seat_str += "%s  " % seat
            label_select_seat.config(text=select_seat_str)
            if len(select_seat_list) < int(spinbox.get()):
                seat_check_fun()
#    
     
    ## 각 좌석에 A1 형식으로 알파벳과 번호 할당
    seat_list=[]
    for x in range(0,5):
        for y in range(0,5):
            seat_list.append("%s%c%d" % ("seat_",alpha[x], number[y])) 
    
    ## 같은 열(알파벳)끼리 묶어서 2차원리스트로 만들기        
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
   
    ## 버튼 배치 및 속성 설정
    for x in range(0,5):
        for y in range(0,5):
            seat_all[x][y] = Button(frame_seat, text=seat_all[x][y][5:7], bd = 5, width = 4, height =2, font = ("굴림", 20, "bold"),state = 'disabled', relief = 'sunken', bg = 'gray', disabledforeground='#C9C9C9', command=partial(seat_fun,x,y)) # 좌석 버튼
            seat_all[x][y].grid(row=x, column=y,padx=10, pady=10)   
  
    
        
      
      
      
      
              
        
    
    # 선택 정보
    
    ## 포스터    
    poster = ImageTk.PhotoImage(file = 'D:\\jjh\\python\\pyworkspace\\MovieSite\\Poster\\blackposter.jpg') # 변수에 이미지 저장
#     poster = ImageTk.PhotoImage(file = 'D:\\Users\\jeong\\Documents\\workspacePython\\MovieSite\\Poster\\blackposter.jpg') # 변수에 이미지 저장
    select_img = Label(frame_selectinfo) # Label에 이미지변수 할당
    select_img.configure(image=poster)
    select_img.image = poster    
    select_img.place(x=37, y = 20)
    
    ## 영화제목
    Label_title = Label(frame_selectinfo, text="영화명:", font=("굴림", 12, "bold"), bg="#FFFF8F", fg="black",) # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
    Label_title.place(x=10, y=350)
    label_select_title = Label(frame_selectinfo, text="", font=("굴림", 13), bg="#FFFF8F", fg="black", justify="left", wraplength=180) # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
    label_select_title.place(x=95, y=350)
    
    ## 상영시간
    Label_time = Label(frame_selectinfo, text="상영시간:", font=("굴림", 12, "bold"), bg="#FFFF8F", fg="black",) # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
    Label_time.place(x=10, y=400)
    label_select_time = Label(frame_selectinfo, text="", font=("굴림", 13), bg="#FFFF8F", fg="black",) # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
    label_select_time.place(x=95, y=400)
    
    ## 관람인원
    Label_people = Label(frame_selectinfo, text="인원:", font=("굴림", 12, "bold"), bg="#FFFF8F", fg="black",) # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
    Label_people.place(x=10, y=450)
    label_select_people = Label(frame_selectinfo, text="1 명", font=("굴림", 13), bg="#FFFF8F", fg="black",) # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
    label_select_people.place(x=95, y=450)
    
    ## 좌석
    Label_seat = Label(frame_selectinfo, text="좌석:", font=("굴림", 12, "bold"), bg="#FFFF8F", fg="black",) # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
    Label_seat.place(x=10, y=500)
    label_select_seat = Label(frame_selectinfo, text="", font=("굴림", 13), bg="#FFFF8F", fg="black",) # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
    label_select_seat.place(x=95, y=500)
    
    ## 결제금액
    Label_price = Label(frame_selectinfo, text="결제금액:", font=("굴림", 12, "bold"), bg="#FFFF8F", fg="black",) # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
    Label_price.place(x=10, y=550)
    label_select_price = Label(frame_selectinfo, text="9000 원", font=("굴림", 13), bg="#FFFF8F", fg="black",) # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
    label_select_price.place(x=95, y=550)
    
    w2.mainloop()
 
 
if __name__ == '__main__':
    call()