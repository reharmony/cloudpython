'''
Created on 2019. 4. 10.

@author: user
'''
from tkinter import *
from db.DB연결테스트 import *

def event_process():
    print("이벤트가 처리 되었음...")
    id = id_input.get() # get()은 값을 스트링으로 가져옴
    pw = pw_input.get() # get()은 값을 스트링으로 가져옴
    name = name_input.get() # get()은 값을 스트링으로 가져옴
    tel = tel_input.get() # get()은 값을 스트링으로 가져옴
    db_process_insert(id,pw,name,tel)
#     print("당신이 입력한 id:", id)



    
w = Tk() # 윈도우 생성

w.geometry("400x600") # 윈도우 크기 설정
w.title("나의 첫 윈도우") # 윈도우 제목 설정
w.resizable(width=False, height=False) # 크기고정
w.configure(bg="#FAF4C0")

id_text = Label(w, text="아이디 입력", font=("굴림", 25), fg="blue", bg="#FAF4C0") # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
pw_text = Label(w, text="패스워드 입력", font=("굴림", 25), fg="blue", bg="#FAF4C0") # 레이블 정의
name_text = Label(w, text="이름 입력", font=("굴림", 25), fg="blue", bg="#FAF4C0") # 레이블 정의
tel_text = Label(w, text="전화번호 입력", font=("굴림", 25), fg="blue", bg="#FAF4C0") # 레이블 정의
CAPT_text = Label(w, text="로봇이 아닌지 확인해야합니다. reCAPTCHA", font=("굴림", 12), fg="blue", bg="#FAF4C0") # 레이블 정의

insert = Button(w, text="회원가입 처리", font = ("굴림", 25), fg = "red", bg= "yellow", command = event_process) # 버튼 정의

id_input = Entry(w, fg = "#F2CB61", font =("굴림",25), width=12) # 입력칸 정의
pw_input = Entry(w, fg = "#F2CB61", font =("굴림",25), width=12) # 입력칸 정의
name_input = Entry(w, fg = "#F2CB61", font =("굴림",25),width=12) # 입력칸 정의
tel_input = Entry(w, fg = "#F2CB61", font =("굴림",25),width=12) # 입력칸 정의





id_text.pack() # 레이블 윈도우에 삽입
id_input.pack() # 입력칸 윈도우에 삽입
pw_text.pack() # 레이블 윈도우에 삽입
pw_input.pack() # 입력칸 윈도우에 삽입
name_text.pack() # 레이블 윈도우에 삽입
name_input.pack() # 입력칸 윈도우에 삽입
tel_text.pack() # 레이블 윈도우에 삽입
tel_input.pack() # 입력칸 윈도우에 삽입

insert.pack() # 버튼 윈도우에 삽입
CAPT_text.pack() # 레이블 윈도우에 삽입



w.mainloop() # 윈도우 유지