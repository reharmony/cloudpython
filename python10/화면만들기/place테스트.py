'''
Created on 2019. 4. 10.

@author: user
'''
from tkinter import *
from db.DB연결_과제0411 import *

id_input, title_input, content_input, director_input, img_input, data, record, label = None, None, None, None, None, None, None, None


def insert_ui():
    
    global id_input,title_input,content_input,director_input, img_input
       
    w = Tk() # 윈도우 생성
    
    w.geometry("400x400") # 윈도우 크기 설정
    w.title("영화 정보 입력") # 윈도우 제목 설정
    w.resizable(width=False, height=False) # 크기고정
    w.configure(bg="#FAF4C0")
    
    id_text = Label(w, text="영화 코드", font=("굴림", 20), fg="blue", bg="#FAF4C0") # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
    title_text = Label(w, text="제목", font=("굴림", 20), fg="blue", bg="#FAF4C0") # 레이블 정의
    content_text = Label(w, text="줄거리", font=("굴림", 20), fg="blue", bg="#FAF4C0") # 레이블 정의
    director_text = Label(w, text="감독", font=("굴림", 20), fg="blue", bg="#FAF4C0") # 레이블 정의
    img_text = Label(w, text="이미지 주소", font=("굴림", 20), fg="blue", bg="#FAF4C0") # 레이블 정의
   
    insert = Button(w, text="입력", font = ("굴림", 15),command = event_process_insert) # 버튼 정의 (tkinter에서는 함수에() 생략)
    
    id_input = Entry(w, fg = "#F2CB61", font =("굴림",20), width=12) # 입력칸 정의
    title_input = Entry(w, fg = "#F2CB61", font =("굴림",20), width=12) # 입력칸 정의
    content_input = Entry(w, fg = "#F2CB61", font =("굴림",20),width=12) # 입력칸 정의
    director_input = Entry(w, fg = "#F2CB61", font =("굴림",20),width=12) # 입력칸 정의   
    img_input = Entry(w, fg = "#F2CB61", font =("굴림",20),width=12) # 입력칸 정의   
    
    id_text.pack() # 레이블 윈도우에 삽입
    id_input.pack() # 입력칸 윈도우에 삽입
    title_text.pack() # 레이블 윈도우에 삽입
    title_input.pack() # 입력칸 윈도우에 삽입
    content_text.pack() # 레이블 윈도우에 삽입
    content_input.pack() # 입력칸 윈도우에 삽입
    director_text.pack() # 레이블 윈도우에 삽입
    director_input.pack() # 입력칸 윈도우에 삽입
    img_text.pack() # 레이블 윈도우에 삽입
    img_input.pack() # 입력칸 윈도우에 삽입
    
    insert.pack() # 버튼 윈도우에 삽입
    
    
    w.mainloop() # 윈도우 유지
    
    
    
def select_result_ui(record):
    
    ######################### 새 창에 이미지 띄울때는 Tk()가 아니라 Toplevel() 써줘야함!!! 중요!!! #######################
    w = Toplevel() 
    w.geometry("600x650") # 윈도우 크기 설정
    w.title("영화 정보 검색 결과") # 윈도우 제목 설정
    w.configure(bg="#FAF4C0")
    
    id_text = Label(w, text="검색된 영화코드", font=("굴림", 20), fg="blue", bg="#FAF4C0") # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
    title_text = Label(w, text="검색된 제목", font=("굴림", 20), fg="blue", bg="#FAF4C0") # 레이블 정의
    content_text = Label(w, text="검색된 줄거리", font=("굴림", 20), fg="blue", bg="#FAF4C0") # 레이블 정의
    director_text = Label(w, text="검색된 감독", font=("굴림", 20), fg="blue", bg="#FAF4C0") # 레이블 정의
    img_text = Label(w, text="검색된  이미지", font=("굴림", 20), fg="blue", bg="#FAF4C0") # 레이블 정의
   
    id_input = Label(w, text=record[0],bg ="white",font =("굴림",20), width=12) # 입력칸 정의
    title_input = Label(w, text=record[1],bg ="white",font =("굴림",20), width=12) # 입력칸 정의
    content_input = Label(w, text=record[2],bg ="white",font =("굴림",20),width=12) # 입력칸 정의
    director_input = Label(w, text=record[3],bg ="white",font =("굴림",20),width=12) # 입력칸 정의
    icon = PhotoImage(file = record[4]) # 변수에 이미지 저장
    img_input = Label(w) # Label에 이미지변수 할당
    img_input.configure(image=icon)
    img_input.image = icon    
    
    id_text.place(x=300, y=0) # 레이블 윈도우에 삽입
    id_input.place(x=300, y=50) # 입력칸 윈도우에 삽입
    title_text.place(x=300, y=100) # 레이블 윈도우에 삽입
    title_input.place(x=300, y=150) # 입력칸 윈도우에 삽입
    content_text.place(x=300,y=200) # 레이블 윈도우에 삽입
    content_input.place(x=300,y=250) # 입력칸 윈도우에 삽입
    director_text.place(x=300,y=300) # 레이블 윈도우에 삽입
    director_input.place(x=300,y=350) # 입력칸 윈도우에 삽입
    img_text.place(x=0,y=0) # 레이블 윈도우에 삽입    
    img_input.place(x=0,y=50) # 레이블 윈도우에 삽입             
        
    w.mainloop() # 윈도우 유지
    
    
def select_ui():
    
    global id_input,title_input,content_input,director_input, img_input, data
    
    w = Tk() # 윈도우 생성
    
    w.geometry("400x150") # 윈도우 크기 설정
    w.title("영화 정보 검색") # 윈도우 제목 설정
    w.resizable(width=False, height=False) # 크기고정
    w.configure(bg="#FAF4C0")
    
    id_text = Label(w, text="검색할 영화의 코드를 입력하세요.", font=("굴림", 17), bg="#FAF4C0") # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
 
    insert = Button(w, text="검색", font = ("굴림", 15), command = event_process_select) # 버튼 정의
    
    data = Entry(w, font =("굴림",25), width=12) # 입력칸 정의   
    
    id_text.pack() # 레이블 윈도우에 삽입
    data.pack() # 입력칸 윈도우에 삽입   
    
    insert.pack() # 버튼 윈도우에 삽입  

    w.mainloop() # 윈도우 유지
    
    
    
def update_ui():
    
    global id_input,title_input,content_input,director_input, img_input
    
    w = Tk() # 윈도우 생성
    
    w.geometry("300x400") # 윈도우 크기 설정
    w.title("영화 정보 수정") # 윈도우 제목 설정
    w.resizable(width=False, height=False) # 크기고정
    w.configure(bg="#FAF4C0")
    
    id_text = Label(w, text="영화 코드", font=("굴림", 20), fg="blue", bg="#FAF4C0") # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
    title_text = Label(w, text="제목", font=("굴림", 20), fg="blue", bg="#FAF4C0") # 레이블 정의
    content_text = Label(w, text="줄거리", font=("굴림", 20), fg="blue", bg="#FAF4C0") # 레이블 정의
    director_text = Label(w, text="감독", font=("굴림", 20), fg="blue", bg="#FAF4C0") # 레이블 정의
    img_text = Label(w, text="이미지 주소", font=("굴림", 20), fg="blue", bg="#FAF4C0") # 레이블 정의
    
    
    insert = Button(w, text="수정", font = ("굴림", 15), command = event_process_update) # 버튼 정의
    
    id_input = Entry(w, fg = "#F2CB61", font =("굴림",20), width=12) # 입력칸 정의
    title_input = Entry(w, fg = "#F2CB61", font =("굴림",20), width=12) # 입력칸 정의
    content_input = Entry(w, fg = "#F2CB61", font =("굴림",20),width=12) # 입력칸 정의
    director_input = Entry(w, fg = "#F2CB61", font =("굴림",20),width=12) # 입력칸 정의   
    img_input = Entry(w, fg = "#F2CB61", font =("굴림",20),width=12) # 입력칸 정의   
    
    id_text.pack() # 레이블 윈도우에 삽입
    id_input.pack() # 입력칸 윈도우에 삽입
    title_text.pack() # 레이블 윈도우에 삽입
    title_input.pack() # 입력칸 윈도우에 삽입
    content_text.pack() # 레이블 윈도우에 삽입
    content_input.pack() # 입력칸 윈도우에 삽입
    director_text.pack() # 레이블 윈도우에 삽입
    director_input.pack() # 입력칸 윈도우에 삽입
    img_text.pack() # 레이블 윈도우에 삽입
    img_input.pack() # 입력칸 윈도우에 삽입
    
    insert.pack() # 버튼 윈도우에 삽입
     
    
    w.mainloop() # 윈도우 유지
    
    
    
def delete_ui():
    
    global id_input
           
    w = Tk() # 윈도우 생성
    
    w.geometry("400x150") # 윈도우 크기 설정
    w.title("영화 정보 삭제") # 윈도우 제목 설정
    w.resizable(width=False, height=False) # 크기고정
    w.configure(bg="#FAF4C0")
    
    id_text = Label(w, text="영화 코드", font=("굴림", 20), fg="blue", bg="#FAF4C0") # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
    
    insert = Button(w, text="삭제", font = ("굴림", 15), command = event_process_delete) # 버튼 정의
    
    id_input = Entry(w, fg = "#F2CB61", font =("굴림",20), width=12) # 입력칸 정의
   
    
    id_text.pack() # 레이블 윈도우에 삽입
    id_input.pack() # 입력칸 윈도우에 삽입   
    
    insert.pack() # 버튼 윈도우에 삽입  
 
    w.mainloop() # 윈도우 유지
    
   
   
   
   
def event_process_insert():
    print("이벤트가 처리 되었음...")
    id = id_input.get() # get()은 값을 스트링으로 가져옴
    title = title_input.get() # get()은 값을 스트링으로 가져옴
    content = content_input.get() # get()은 값을 스트링으로 가져옴
    director = director_input.get() # get()은 값을 스트링으로 가져옴
    img = img_input.get() # get()은 값을 스트링으로 가져옴
    db_process_insert(id,title,content,director,img)

    
def event_process_select():
    global data, record
    print("정보검색 시작...")
    id = data.get() # get()은 값을 스트링으로 가져옴   
    record = db_process_select(id)
    select_result_ui(record)

    
def event_process_update():
    print("이벤트가 처리 되었음...")
    id = id_input.get() # get()은 값을 스트링으로 가져옴
    title = title_input.get() # get()은 값을 스트링으로 가져옴
    content = content_input.get() # get()은 값을 스트링으로 가져옴
    director = director_input.get() # get()은 값을 스트링으로 가져옴
    img = img_input.get() # get()은 값을 스트링으로 가져옴
    db_process_update(id,title,content,director,img)

    
def event_process_delete():
    print("이벤트가 처리 되었음...")
    id = id_input.get() # get()은 값을 스트링으로 가져옴  
    db_process_delete(id)
    
    
    
if __name__ == '__main__':
    
    w = Tk() # 윈도우 생성
    
    w.geometry("300x250") # 윈도우 크기 설정
    w.title("영화 정보 관리 프로그램") # 윈도우 제목 설정
    w.resizable(width=False, height=False) # 크기고정
    w.configure(bg="#FAF4C0")
    
    insert = Button(w, text="영화정보 입력", font = ("굴림", 20),command = insert_ui, overrelief = 'solid') # 버튼 정의
    insert.pack() # 버튼 윈도우에 삽입
    insert = Button(w, text="영화정보 검색", font = ("굴림", 20),command = select_ui) # 버튼 정의
    insert.pack() # 버튼 윈도우에 삽입
    insert = Button(w, text="영화정보 수정", font = ("굴림", 20),command = update_ui) # 버튼 정의
    insert.pack() # 버튼 윈도우에 삽입
    insert = Button(w, text="영화정보 삭제", font = ("굴림", 20),command = delete_ui) # 버튼 정의
    insert.pack() # 버튼 윈도우에 삽입
    
    
    w.mainloop() # 윈도우 유지
    
   