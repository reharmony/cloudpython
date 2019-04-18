'''
Created on 2019. 4. 10.

@author: user
'''
from tkinter import *
from db.DB연결테스트 import *

id_input, pw_input, name_input, tel_input, data, record = None, None, None, None, None, None

def insert_ui():
    
    global id_input,pw_input,name_input,tel_input
       
    w = Tk() # 윈도우 생성
    
    w.geometry("400x400") # 윈도우 크기 설정
    w.title("나의 첫 윈도우") # 윈도우 제목 설정
    w.resizable(width=False, height=False) # 크기고정
    w.configure(bg="#FAF4C0")
    
    id_text = Label(w, text="아이디 입력", font=("굴림", 25), fg="blue", bg="#FAF4C0") # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
    pw_text = Label(w, text="패스워드 입력", font=("굴림", 25), fg="blue", bg="#FAF4C0") # 레이블 정의
    name_text = Label(w, text="이름 입력", font=("굴림", 25), fg="blue", bg="#FAF4C0") # 레이블 정의
    tel_text = Label(w, text="전화번호 입력", font=("굴림", 25), fg="blue", bg="#FAF4C0") # 레이블 정의
   
    insert = Button(w, text="회원 가입", font = ("굴림", 25), fg = "red", bg= "yellow", command = event_process_insert) # 버튼 정의 (tkinter에서는 함수에() 생략)
    
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
    
    
    w.mainloop() # 윈도우 유지
    
    
    
def select_result_ui(record):
    
    w = Tk() # 윈도우 생성
    
    w.geometry("400x400") # 윈도우 크기 설정
    w.title("나의 첫 윈도우") # 윈도우 제목 설정
    w.resizable(width=False, height=False) # 크기고정
    w.configure(bg="#FAF4C0")
    
    id_text = Label(w, text="검색된 아이디", font=("굴림", 25), fg="blue", bg="#FAF4C0") # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
    pw_text = Label(w, text="검색된 암호", font=("굴림", 25), fg="blue", bg="#FAF4C0") # 레이블 정의
    name_text = Label(w, text="검색된 이름", font=("굴림", 25), fg="blue", bg="#FAF4C0") # 레이블 정의
    tel_text = Label(w, text="검색된 전화번호", font=("굴림", 25), fg="blue", bg="#FAF4C0") # 레이블 정의
   
    id_input = Label(w, text=record[0],bg ="white",font =("굴림",25), width=12) # 입력칸 정의
    pw_input = Label(w, text=record[1],bg ="white",font =("굴림",25), width=12) # 입력칸 정의
    name_input = Label(w, text=record[2],bg ="white",font =("굴림",25),width=12) # 입력칸 정의
    tel_input = Label(w, text=record[3],bg ="white",font =("굴림",25),width=12) # 입력칸 정의   
    
    id_text.pack() # 레이블 윈도우에 삽입
    id_input.pack() # 입력칸 윈도우에 삽입
    pw_text.pack() # 레이블 윈도우에 삽입
    pw_input.pack() # 입력칸 윈도우에 삽입
    name_text.pack() # 레이블 윈도우에 삽입
    name_input.pack() # 입력칸 윈도우에 삽입
    tel_text.pack() # 레이블 윈도우에 삽입
    tel_input.pack() # 입력칸 윈도우에 삽입
        
    w.mainloop() # 윈도우 유지
    
    
def select_ui():
    
    global id_input,pw_input,name_input,tel_input,data
    
    w = Tk() # 윈도우 생성
    
    w.geometry("400x150") # 윈도우 크기 설정
    w.title("나의 첫 윈도우") # 윈도우 제목 설정
    w.resizable(width=False, height=False) # 크기고정
    w.configure(bg="#FAF4C0")
    
    id_text = Label(w, text="검색할 ID를 입력하세요.", font=("굴림", 20), bg="#FAF4C0") # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
 
    insert = Button(w, text="검색", font = ("굴림", 15), command = event_process_select) # 버튼 정의
    
    data = Entry(w, font =("굴림",25), width=12) # 입력칸 정의   
    
    id_text.pack() # 레이블 윈도우에 삽입
    data.pack() # 입력칸 윈도우에 삽입   
    
    insert.pack() # 버튼 윈도우에 삽입  
    
    w.mainloop() # 윈도우 유지
    
    
    
def update_ui():
    
    global id_input
    global pw_input
    global name_input
    global tel_input
    w = Tk() # 윈도우 생성
    
    w.geometry("400x400") # 윈도우 크기 설정
    w.title("나의 첫 윈도우") # 윈도우 제목 설정
    w.resizable(width=False, height=False) # 크기고정
    w.configure(bg="#FAF4C0")
    
    id_text = Label(w, text="아이디 입력", font=("굴림", 25), fg="blue", bg="#FAF4C0") # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
    pw_text = Label(w, text="패스워드 입력", font=("굴림", 25), fg="blue", bg="#FAF4C0") # 레이블 정의
    name_text = Label(w, text="이름 입력", font=("굴림", 25), fg="blue", bg="#FAF4C0") # 레이블 정의
    tel_text = Label(w, text="전화번호 입력", font=("굴림", 25), fg="blue", bg="#FAF4C0") # 레이블 정의
    
    
    insert = Button(w, text="회원 정보 수정", font = ("굴림", 25), fg = "red", bg= "yellow", command = event_process_update) # 버튼 정의
    
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
     
    
    w.mainloop() # 윈도우 유지
    
    
    
def delete_ui():
    
    global id_input
    global pw_input
    global name_input
    global tel_input
       
    w = Tk() # 윈도우 생성
    
    w.geometry("400x150") # 윈도우 크기 설정
    w.title("나의 첫 윈도우") # 윈도우 제목 설정
    w.resizable(width=False, height=False) # 크기고정
    w.configure(bg="#FAF4C0")
    
    id_text = Label(w, text="아이디 입력", font=("굴림", 25), fg="blue", bg="#FAF4C0") # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
    
    insert = Button(w, text="회원 정보 삭제", font = ("굴림", 25), fg = "red", bg= "yellow", command = event_process_delete) # 버튼 정의
    
    id_input = Entry(w, fg = "#F2CB61", font =("굴림",25), width=12) # 입력칸 정의
   
    
    id_text.pack() # 레이블 윈도우에 삽입
    id_input.pack() # 입력칸 윈도우에 삽입   
    
    insert.pack() # 버튼 윈도우에 삽입  
    
    w.mainloop() # 윈도우 유지
    
    
def selectall_ui():
   
    w = Tk() # 윈도우 생성
    
    w.geometry("400x600") # 윈도우 크기 설정
    w.title("나의 첫 윈도우") # 윈도우 제목 설정
    w.resizable(width=False, height=False) # 크기고정
    w.configure(bg="#FAF4C0")
    
    insert = Button(w, text="회원 전체 목록 보기", font = ("굴림", 25), fg = "red", bg= "yellow", command = event_process_selectall) # 버튼 정의 
    insert.pack() # 버튼 윈도우에 삽입   
    allList = db_process_selectall()
    listtext = Label(w, text=allList, font=("굴림", 25), fg="blue", bg="#FAF4C0")
    listtext.pack()    
    
    w.mainloop() # 윈도우 유지
        
    
    
def event_process_insert():
    print("이벤트가 처리 되었음...")
    id = id_input.get() # get()은 값을 스트링으로 가져옴
    pw = pw_input.get() # get()은 값을 스트링으로 가져옴
    name = name_input.get() # get()은 값을 스트링으로 가져옴
    tel = tel_input.get() # get()은 값을 스트링으로 가져옴
    db_process_insert(id,pw,name,tel)

    
def event_process_select():
    global data, record
    print("정보검색 시작...")
    id = data.get() # get()은 값을 스트링으로 가져옴   
    record = db_process_select(id)
    select_result_ui(record)

    
def event_process_update():
    print("이벤트가 처리 되었음...")
    id = id_input.get() # get()은 값을 스트링으로 가져옴
    pw = pw_input.get() # get()은 값을 스트링으로 가져옴
    name = name_input.get() # get()은 값을 스트링으로 가져옴
    tel = tel_input.get() # get()은 값을 스트링으로 가져옴
    db_process_update(id,pw,name,tel)

    
def event_process_delete():
    print("이벤트가 처리 되었음...")
    id = id_input.get() # get()은 값을 스트링으로 가져옴  
    db_process_delete(id)

def event_process_selectall():
    print("이벤트가 처리 되었음...")
    db_process_selectall()
    
    
    
if __name__ == '__main__':
    
    w = Tk() # 윈도우 생성
    
    w.geometry("400x350") # 윈도우 크기 설정
    w.title("메인화면") # 윈도우 제목 설정
    w.resizable(width=False, height=False) # 크기고정
    w.configure(bg="#FAF4C0")
    
    insert = Button(w, text="회원 가입 하기", font = ("굴림", 25), fg = "red", bg= "yellow", command = insert_ui) # 버튼 정의
    insert.pack() # 버튼 윈도우에 삽입
    insert = Button(w, text="회원 검색 하기", font = ("굴림", 25), fg = "red", bg= "yellow", command = select_ui) # 버튼 정의
    insert.pack() # 버튼 윈도우에 삽입
    insert = Button(w, text="회원 수정 하기", font = ("굴림", 25), fg = "red", bg= "yellow", command = update_ui) # 버튼 정의
    insert.pack() # 버튼 윈도우에 삽입
    insert = Button(w, text="회원 탈퇴 하기", font = ("굴림", 25), fg = "red", bg= "yellow", command = delete_ui) # 버튼 정의
    insert.pack() # 버튼 윈도우에 삽입
    insert = Button(w, text="회원 전체 보기", font = ("굴림", 25), fg = "red", bg= "yellow", command = selectall_ui) # 버튼 정의
    insert.pack() # 버튼 윈도우에 삽입
    
    w.mainloop() # 윈도우 유지
    
   