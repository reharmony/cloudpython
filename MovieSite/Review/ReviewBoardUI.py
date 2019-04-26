import tkinter
import pymysql
from Review.WriteReview import *
from Review.DB_select_delete_review import *
from TkTreectrl import *
from Review.ReadReviewUI import *
from tkinter.font import BOLD
from tkinter import messagebox
import TkTreectrl
from Main import Main_UI

w = None

def review_write():
    Insert_Review()

def endCall3():
    global w2
    w.destroy()
    Main_UI.recall()

    

def Review_board_call():
    global w
    w = Tk()
    w.geometry("800x800+500+130")
    w.resizable(width = False, height = False)
    w.title('리뷰 게시판')
    w.configure(bg = '#FFFF8F')
        
    
    frame3=tkinter.Frame(w,relief="solid", bd=3)
    frame3.place(x= 30, y = 60)
        
    
    con = pymysql.connect(host ='13.209.92.229', user = 'root', password = '1234', db = 'cloud')
    cur = con.cursor()
    movie = Listbox(frame3, selectmode='single', width = 56, height=24, font=("굴림",19), fg='black', bd=0)
    
    sql = "select boardnum, reviewtitle, id from reviewboard"
    result = cur.execute(sql)
    recode = cur.fetchall()
    movie.config() 
    
    num_text = Label(w, text='번호', font=('굴림', 20), bg = '#FFFF8F')
    title_text = Label(w, text='제목', font=('굴림', 20), bg = '#FFFF8F')
    id_text = Label(w, text='ID', font=('굴림', 20), bg = '#FFFF8F')
    write_btn = Button(w, text='글쓰기', font=('굴림', 20, 'bold'), fg='white', bg='red', command = review_write)
    cancel_btn = Button(w, text='취소', font=('굴림', 20), command=endCall3)


    def title_fun(event):
        w = event.widget
        index = int(w.curselection()[0])
        titlemovie = w.get(index)
        print('A',titlemovie)
        print('B',titlemovie[2:4])
        readReview(titlemovie[2:4])
    
    movie.bind('<<ListboxSelect>>', title_fun)
    movie.pack()
    num_text.place(x = 30, y = 20)
    title_text.place(x = 300, y = 20)
    id_text.place(x = 610, y = 20)
    write_btn.place(x = 555, y = 720)
    cancel_btn.place(x = 685, y = 720)
    
    for row in recode:
        print(row)
        print(row[0])
        boardTitle = '  %d               %s          %s' %(row[0], row[1], row[2])
        movie.insert(END, boardTitle)
      
    
     
            
    w.mainloop()
    
if __name__ == '__main__':
    Review_board_call()