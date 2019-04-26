from pymysql import *
from tkinter import *
from Review.DB_select_delete_review import review_insert
from tkinter.font import BOLD
from tkinter import messagebox
import gettext
boardnum_input = None
reviewtitle_input, id_input , title_input, reviewcontent_input = '', '' ,'' ,''

def update_review():
    global boardnum_input ,reviewtitle_input, id_input , title_input, reviewcontent_input
    reviewtitle = reviewtitle_input.get()
    reviewcontent = reviewcontent_input.get(1.0, 50.100)
    id = id_input.get()
    movietitle =  title_input.get()
    
    review_insert(reviewtitle, reviewcontent, id, movietitle)
    ok = messagebox.showinfo('완료', '올라갔습니다.')
    
    
    
def Insert_Review():
    global boardnum_input ,reviewtitle_input, id_input , title_input, reviewcontent_input
    w = Tk()
    w.geometry("550x730+600+150")
    w.title('리뷰 쓰기')
    w.configure(bg = '#FFFF8F')
        
            
    
    reviewtitle_text = Label(w, text='제목', font=('굴림', 15, BOLD), bg = '#FFFF8F')
    reviewcontent_text = Label(w, text='내용', font=('굴림', 15, BOLD), bg = '#FFFF8F')
    id_text = Label(w, text='아이디', font=('굴림', 15, BOLD), bg = '#FFFF8F')
    title_text = Label(w, text='영화이름', font=('굴림', 15, BOLD), bg = '#FFFF8F')
    
            
    
   
    reviewtitle_input = Entry(w, font=('굴림', 15), fg = 'black', width=35)
    reviewcontent_input = Text(w, font=('굴림', 15), fg = 'black', width=600)
    id_input = Entry(w, font=('굴림', 15), fg = 'black', width=10)
    title_input = Entry(w, font=('굴림', 15), fg = 'black', width=10)
    
        
        
    insert = Button(w, text='올리기', font=('굴림', 20), fg = 'black',command=update_review)
            
        
   
    reviewtitle_text.pack()
    reviewtitle_input.pack() 
    reviewcontent_text.pack()
    reviewcontent_input.pack()
    id_text.pack()     
    id_input.pack() 
    title_text.pack() 
    title_input.pack()
    
    insert.place(x = 222, y = 680)
    
    
    w.mainloop()

if __name__ == '__main__':
    Insert_Review()