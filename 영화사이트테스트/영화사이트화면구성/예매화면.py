'''
Created on 2019. 4. 17.

@author: user
'''
from tkinter import *
from 영화사이트화면구성 import 메인화면
from string import ascii_uppercase

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
    frame_list=Frame(w2, relief="solid", bd=2, width = 400, height=300)
    frame_list.place(x=50,y=80)
    frame_people=LabelFrame(w2, text="관람 인원", font=('굴림',15), pady=10,relief="solid", bd=2, width = 407, height=330)
    frame_people.place(x=50,y=370)
    frame_time=LabelFrame(w2, text="상영 시간",font=('굴림',15),relief="solid", bd=2, width = 600, height=650, padx=10, pady=10)
    frame_time.place(x=50,y=470)
    frame_seat=LabelFrame(w2, text="좌석 선택", font=('굴림',15),relief="solid", bd=2, width = 600, height=650, padx=20, pady=70)
    frame_seat.place(x=500,y=50)
    frame_selectinfo=Frame(w2, relief="solid", bd=2, width = 300, height=650)
    frame_selectinfo.place(x=1150,y=50)
    
    # 영화 목록 타이틀
    list_title = Label(w2, text="관람할 영화 선택", font=("굴림", 15)) # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
    list_title.place(x=50, y=50)
    
    # 영화 목록 리스트박스
    listbox = Listbox(frame_list, selectmode='single', width = 31, height=10, font=("굴림",19), activestyle='none', fg='white',bg='#191d1f')
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
    
    # 관람인원 스핀박스
    select_people=Label(frame_people)
    select_people.pack()
    
    def value_check(self):
        select_people.config(font=("굴림",1))
        valid = False
        if self.isdigit():
            if (int(self) <= 10 and int(self) >= 1):
                valid = True
        elif self == '':
            valid = True
        return valid
    
    def value_error(self):
        select_people.config(text=str(self) + "를 입력하셨습니다.\n올바른 값을 입력하세요.")
    
    validate_command=(frame_people.register(value_check), '%P')
    invalid_command=(frame_people.register(value_error), '%P')
    
    spinbox=Spinbox(frame_people, from_ = 0, to = 10, width=29, font=("굴림",19),validate = 'all', validatecommand = validate_command, invalidcommand=invalid_command)
    spinbox.pack()
        
    # 상영 시간 라디오 버튼
    RadioVariety_1=IntVar()
             
    radio1=Radiobutton(frame_time, text="09:00",font=("굴림",19), value=1, variable=RadioVariety_1)
    radio1.grid(row=0, column=0, padx= 15, pady=15)
    radio2=Radiobutton(frame_time, text="10:35",font=("굴림",19), value=2, variable=RadioVariety_1)
    radio2.grid(row=0, column=1, padx= 15, pady=15)
    radio3=Radiobutton(frame_time, text="12:10",font=("굴림",19), value=3, variable=RadioVariety_1)
    radio3.grid(row=0, column=2, pady=15)
    radio4=Radiobutton(frame_time, text="14:35",font=("굴림",19), value=4, variable=RadioVariety_1)
    radio4.grid(row=1, column=0, padx= 15, pady=15)
    radio5=Radiobutton(frame_time, text="16:50",font=("굴림",19), value=5, variable=RadioVariety_1)
    radio5.grid(row=1, column=1, padx= 15, pady=15)
    radio6=Radiobutton(frame_time, text="18:25",font=("굴림",19), value=6, variable=RadioVariety_1)
    radio6.grid(row=1, column=2, padx= 15, pady=15)
    radio6=Radiobutton(frame_time, text="19:50",font=("굴림",19), value=7, variable=RadioVariety_1)
    radio6.grid(row=2, column=0, pady=15)
    radio6=Radiobutton(frame_time, text="21:30",font=("굴림",19), value=8, variable=RadioVariety_1)
    radio6.grid(row=2, column=1, padx= 15, pady=15)
    radio6=Radiobutton(frame_time, text="23:15",font=("굴림",19), value=9, variable=RadioVariety_1)
    radio6.grid(row=2, column=2, pady=15)
        
            
        
        
    # 좌석도 버튼
    alpha = list(ascii_uppercase)
    number = list(range(1,101))
    
    # alphabet
    seat_list=[]
    for x in range(0,5):
        for y in range(0,5):
            seat_list.append("%s%c%d" % ("seat_",alpha[x], number[y])) 
    print(seat_list)

    
    def press():
        seat_all[x][y].config(relief='sunken', state='active')
        print("눌렸음")
        

        
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
            seat_all[x][y] = Button(frame_seat, text=seat_all[x][y][5:7], bd = 5, width = 7, height =3, font = ("굴림", 15),relief = 'raised', overrelief = 'solid', state='normal', activebackground='gray', command=press) # 좌석 버튼
            seat_all[x][y].grid(row=x, column=y,padx=10, pady=10)   
    
    
    
    
    
    
    
    
#     button1=Button(frame1, text="프레임1")
#     button1.place(x=10, y=10)
     
#     button2=tkinter.Button(frame2, text="프레임2")
#     button2.pack(side="left")
#     
    
    
    w2.mainloop()
