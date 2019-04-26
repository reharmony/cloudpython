import pymysql
import tkinter
from tkinter import *
from Review.DB_select_delete_review import review_select
from tkinter.font import BOLD
from tkinter import messagebox
from Review.DB_select_delete_review import review_delete
delreview_input = ''

def delete_event2():
    global delreview_input
    boardnum = str(delreview_input.get())
    print(boardnum)
    print(type(boardnum))
    con = pymysql.connect(host ='13.209.92.229', user = 'root', password = '1234', db = 'cloud')
    print('연결 성공')
    print(con)
    cur = con.cursor()
    print(cur)
    sql = "delete from reviewboard where boardnum =" + boardnum
    print(sql)
    cur.execute(sql)
    print('전송 성공')
    con.commit()
    messagebox.showinfo('', '삭제 되었습니다.')
    con.close()


def readReview(titlemovie):
    con = pymysql.connect(host ='13.209.92.229', user = 'root', password = '1234', db = 'cloud')
    print(con)
    cur = con.cursor()
    print(cur)
    inttile = int(titlemovie)
    sql = "select * from reviewboard where boardnum =%d" % inttile 
    result = cur.execute(sql)
    print('sql문 실행결과: ', result)
    print('전송 성공')
    con.commit()
    recode = cur.fetchone()
    
    print(recode)    
    con.commit()
    con.close()
    print('연결해제')
    
        
    number = recode[0]
    title = recode[1]
    content = recode[2]
    id = recode[3]
    movie_title = recode[4]

    k = Tk()
    k.geometry("650x750+530+150")
    k.title('리뷰게시판')
    k.resizable(width = False, height = False)  
    frame=tkinter.Frame(k,width =630, height = 30, relief="solid", bd=2)
    title_text = Label(frame, text=title, font=('굴림', 15, BOLD))
    frame4=tkinter.Frame(k,width = 630, height = 550, relief="solid", bd=2)
    content_text = Label(frame4, text=content, font=('굴림', 10, BOLD))
    frame9=tkinter.Frame(k,width = 250, height = 30, relief="solid", bd=2)
    id_text = Label(frame9, text=id, font=('굴림', 15))
    id_text2 = Label(frame9, text='아이디:', font=('굴림', 15, BOLD))
    frame8=tkinter.Frame(k,width = 350, height = 30, relief="solid", bd=2)
    movie_title_text = Label(frame8, text=movie_title, font=('굴림', 15))
    movie_title_text2 = Label(frame8, text='리뷰 영화 :', font=('굴림', 15, BOLD))
    
    
    def close_event():
        k.destroy()
    ok_btn = Button(k, text='확인', font=('굴림', 15, BOLD), bg = 'green', fg = 'yellow', command = close_event)
    

    

    def delete_event1():
        global delreview_input
        answer = messagebox.askquestion('글 삭제', '글을 삭제 하시겠습니까?')
        if answer == 'no':
            k.destroy()
        elif answer == 'yes':
            global delreview_input
            win = Tk()
            win.geometry("300x70+700+350")
            win.title('글 삭제')
            win.resizable(width = False, height = False)
            del_text = Label(win, text='삭제를 위해  게시물 번호를 입력해 주세요.', font=('굴림', 10, BOLD))
            delreview_input = Entry(win, font=('굴림', 10), fg = 'black', width=20)
            delete_btn = Button (win, text='삭제', font=('굴림', 10, BOLD), command = delete_event2)
            del_text.pack()
            delreview_input.pack()
            delete_btn.pack()
            k.destroy()
                
            win.mainloop()    
    del_btn = Button(k, text='삭제', font=('굴림', 15, BOLD), bg = 'yellow', fg = 'red', command = delete_event1)
                
                
                
    frame.place(x=10,y=20)
    title_text.place(x=8,y=0)
    frame9.place(x=10,y=75)
    id_text.place(x=85,y=0)
    id_text2.place(x=8,y=0)
    frame4.place(x=10,y=143)
    content_text.place(x=5,y=5)
    frame8.place(x=290,y=75)
    movie_title_text.place(x=120,y=0)
    movie_title_text2.place(x=8,y=0)
    ok_btn.place(x=200,y=700)
    del_btn.place(x=400, y=700)
                
                
    k.mainloop()