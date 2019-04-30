'''
Created on 2019. 4. 30.

@author: jeong
'''

from tkinter import *
from tkinter import messagebox
from cloud.DB_insert import * 
from cloud.DB_update import * 
from cloud.DB_select_static import * 
from cloud.DB_select_all import * 

#  글로벌 변수 선언
w, id, subject, content, price, people, w_ins, w_sel, w_upd, w_sta = None, None, None, None, None, None, None, None, None, None


# 입력버튼 클릭시 이벤트
def insert_fun():
    global id_entry, subject_entry, content_entry, price_entry, people_entry, w_ins
    
    id = id_entry.get()
    subject = subject_entry.get()
    content = content_entry.get()
    price = price_entry.get()
    people = people_entry.get()
    
    print(id,subject,content,price,people)
    db_process_insert(id, subject, content, price, people)
    
    w_ins.destroy()


# 수정버튼 클릭시 이벤트    
def update_fun():
    global id_entry, price_entry, w_upd
    
    id = id_entry.get()   
    price = price_entry.get()
    
    print(id,price)
    db_process_update(id, price)
    
    w_upd.destroy()
    
    
# 입력창
def insert_win():
    global w_ins, id_entry, subject_entry, content_entry, price_entry, people_entry
    w_ins = Toplevel()
    w_ins.title('수강 정보 입력')
    w_ins.geometry('250x150+800+250')
    
    id_label = Label(w_ins, text='수강아이디')
    id_entry = Entry(w_ins)
    subject_label = Label(w_ins, text='수강과목')
    subject_entry = Entry(w_ins)
    content_label = Label(w_ins, text='수강내용')
    content_entry = Entry(w_ins)
    price_label = Label(w_ins, text='수강비용')
    price_entry = Entry(w_ins)
    people_label = Label(w_ins, text='수강가능인원')
    people_entry = Entry(w_ins)
    
    id_label.grid(row=0,column=0)
    id_entry.grid(row=0,column=1)
    subject_label.grid(row=1,column=0)
    subject_entry.grid(row=1,column=1)
    content_label.grid(row=2,column=0)
    content_entry.grid(row=2,column=1)
    price_label.grid(row=3,column=0)
    price_entry.grid(row=3,column=1)
    people_label.grid(row=4,column=0)
    people_entry.grid(row=4,column=1)
     
    insert_db_button = Button(w_ins, text='입력', command=insert_fun)
    insert_db_button.grid(row=5, column=1)
 
    w_ins.mainloop()
    
    
# 출력창    
def select_win():
    w_sel = Toplevel()
    w_sel.title('수강 정보 출력')
    w_sel.geometry('400x150+800+250')
    
    result = db_process_select_all()
    
    id_label = Label(w_sel, text='수강아이디', fg='red')    
    subject_label = Label(w_sel, text='수강과목', fg='red')    
    content_label = Label(w_sel, text='수강내용', fg='red')    
    price_label = Label(w_sel, text='수강비용', fg='red')    
    people_label = Label(w_sel, text='수강가능인원', fg='red')   
    
    id_label.grid(row=0,column=0)    
    subject_label.grid(row=0,column=1)    
    content_label.grid(row=0,column=2)    
    price_label.grid(row=0,column=3)    
    people_label.grid(row=0,column=4)
    
    x = 1
    for record in result:    
        id_result = Label(w_sel, text=record[0])
        subject_result = Label(w_sel,text=record[1])
        content_result = Label(w_sel, text=record[2])
        price_result = Label(w_sel, text=record[3])
        people_result = Label(w_sel, text=record[4])
            
        id_result.grid(row=x,column=0)
        subject_result.grid(row=x,column=1)
        content_result.grid(row=x,column=2)
        price_result.grid(row=x,column=3)
        people_result.grid(row=x,column=4)
        
        x = x + 1
    
    w_sel.mainloop()
    
    
# 수정창    
def update_win():
    global w_upd, id_entry, subject_entry, content_entry, price_entry, people_entry
    
    w_upd = Toplevel()
    w_upd.title('수강 정보 수정')
    w_upd.geometry('250x150+800+250')
    
    id_label = Label(w_upd, text='수강아이디')
    id_entry = Entry(w_upd)    
    price_label = Label(w_upd, text='수강비용')
    price_entry = Entry(w_upd)
        
    id_label.grid(row=0,column=0)
    id_entry.grid(row=0,column=1)   
    price_label.grid(row=1,column=0)
    price_entry.grid(row=1,column=1)
    
    
    update_db_button = Button(w_upd, text='수정', command=update_fun)
    update_db_button.grid(row=2, column=1)
    
    w_upd.mainloop()
    
    
# 정리창    
def static_win():
    w_sta = Toplevel()
    w_sta.title('수강 비용 정리')
    w_sta.geometry('250x150+800+250')
    
    result = db_process_select_static()
    
    sum = result[0][0]
    avg = result[1][0]
    
    sum_label = Label(w_sta, text='수강비용 합계', fg='red')
    sum_value = Label(w_sta, text="%d원" % sum)
    avg_label = Label(w_sta, text='수강비용 평균', fg='red')
    avg_value = Label(w_sta, text="%d원" % int(avg))
    
    sum_label.grid(row=0,column=0)
    sum_value.grid(row=0,column=1)
    avg_label.grid(row=1,column=0)
    avg_value.grid(row=1,column=1)
        
    w_sta.mainloop()
    
    
# 종료메세지
def end_info():
    global w
    if messagebox.askokcancel('INFO', '프로그램을 종료하시겠습니까?'):
        w.destroy()
    else:
        pass
    
    
# 메인창
def Open_window():
    global w
    w = Tk()
    w.geometry('300x150+800+250')
    w.title('수강과목 관리 프로그램')
    
    insert_button = Button(w,text="1. 입력", command=insert_win)        
    insert_button.pack()
    
    select_button = Button(w,text="2. 출력", command=select_win)        
    select_button.pack()
    
    update_button = Button(w,text="3. 수정", command=update_win)        
    update_button.pack()
    
    static_button = Button(w,text="4. 정리", command=static_win)        
    static_button.pack()
    
    end_button = Button(w,text="5. 종료", command=end_info)        
    end_button.pack()
    
    w.mainloop()
    

if __name__ == '__main__':
    # 프로그램 시작시 메인창 실행
    Open_window()