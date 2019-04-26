from tkinter import *
from Signup.DB_insert_member import *
from Signup import DB_insert_member
from tkinter.font import BOLD
from tkinter import messagebox
id_input, pw_input, name_input, tel_input, email_input, birth_input, gender_input = None, None, None, None, None, None, None
label, w = None, None

def insert_member():
    global w
    id = id_input.get()
    pw = pw_input.get()
    name = name_input.get()
    tel = tel_input.get()
    email = email_input.get()
    birth = birth_input.get()
    gender = gender_input.get()
    DB_insert_member.insert_member(id, pw, name, tel, email, birth, gender)
    w.destroy()
    
    
    
def ID_event():
    global id_input, pw_input, w
     
    id = id_input.get()
    
    
    print(id)
    
    con = pymysql.connect(host ='13.209.92.229', user = 'root', password = '1234', db = 'cloud')
    print('DB인증 >> 연결 성공...')
    print(con)
    
    cur = con.cursor()
    print(cur)
    
    sql = "select * from member where id = ('" + id + "')"
    
    result = cur.execute(sql)
    print('sql문 실행결과: ', result)
    print('전송 성공')
    con.commit()
    
   
    recode = cur.fetchone()
    
   

    print(list)
    
    if recode != None:
        if id == recode[0]:
            messagebox.showerror('아이디 중복 체크', '사용중인 아이디 입니다.')
    else:
        messagebox.showinfo('아이디 중복 체크', '사용가능한 아이디 입니다.')
   
    con.close()
    print('연결해제')
    w.lift()

def member_insert():  
    global  id_input, pw_input, name_input, tel_input, email_input, birth_input, gender_input, label, w
    w = Toplevel()
    w.geometry("350x300+800+250")
    w.title('회원가입')
    w.configure(bg = '#FFFF8F')
    intro = Label(w, text='회원가입\n', font=('굴림', 20, BOLD), bg = '#FFFF8F')
        
    id_text = Label(w, text='ID', font=('굴림', 15, BOLD), fg = 'blue', bg = '#FFFF8F')
    
    pw_text = Label(w, text='비밀번호 ', font=('굴림', 15, BOLD), fg = 'blue', bg = '#FFFF8F')
    name_text = Label(w, text='이름 ', font=('굴림', 15, BOLD), fg = 'blue', bg = '#FFFF8F')
    tel_text = Label(w, text='전화번호 ', font=('굴림', 15, BOLD), fg = 'blue', bg = '#FFFF8F')
    email_text = Label(w, text='이메일 ', font=('굴림', 15, BOLD), fg = 'blue', bg = '#FFFF8F')
    birth_text = Label(w, text='생년월일 ', font=('굴림', 15, BOLD), fg = 'blue', bg = '#FFFF8F')
    gender_text = Label(w, text='성별', font=('굴림', 15, BOLD), fg = 'blue', bg = '#FFFF8F')
        
        
    id_input = Entry(w, font=('굴림', 15), fg = 'black', width=10)
    pw_input = Entry(w, font=('굴림', 15), fg = 'black', width=10, show='●')
    name_input = Entry(w, font=('굴림', 15), fg = 'black', width=10)
    tel_input = Entry(w, font=('굴림', 15), fg = 'black', width=10)
    email_input = Entry(w, font=('굴림', 15), fg = 'black', width=20)
    birth_input = Entry(w, font=('굴림', 15), fg = 'black', width=10)
    gender_input = Entry(w, font=('굴림', 15), fg = 'black', width=5)
    
    insert = Button(w,width= 160,height= 40,command=insert_member)
    img_insert = PhotoImage(file="D:\\jjh\\python\\pyworkspace\\MovieSite\\design\\Signup_Button.png").subsample(3) 
#     img_insert = PhotoImage(file="D:\\JYS\\movieSite\\UI\\Signup_Button.png").subsample(3) 
    insert.config(image=img_insert)
    
    insert2 = Button(w, width= 70, height= 20,  command=ID_event)
    img_insert2 = PhotoImage(file="D:\\jjh\\python\\pyworkspace\\MovieSite\\design\\Signup_Button2.png").subsample(5) 
#     img_insert2 = PhotoImage(file="D:\\JYS\\movieSite\\UI\\Signup_Button2.png").subsample(5) 
    insert2.config(image=img_insert2)    
    
            
    intro.pack()
    id_text.place(x= 10, y = 30)
    id_input.place(x= 100, y = 30)
    pw_text.place(x = 10, y = 60)
    pw_input.place(x = 100, y = 60)
    name_text.place(x = 10, y = 90)
    name_input.place(x = 100, y = 90)
    tel_text.place(x = 10, y = 120)
    tel_input.place(x = 100, y = 120)
    email_text.place(x = 10, y = 150)
    email_input.place(x = 100, y = 150)
    birth_text.place(x = 10, y = 180)
    birth_input.place(x = 100, y = 180)
    gender_text.place(x = 10, y = 210)
    gender_input.place(x = 100, y = 210)
    insert.place(x = 95, y = 240)
    insert2.place(x = 240, y = 30)
    w.mainloop()
    
if __name__ == '__main__':
    member_insert()