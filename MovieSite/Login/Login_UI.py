import pymysql
from tkinter import *
from tkinter import messagebox
from Login.DB_Login import *
from tkinter.font import BOLD
# from Login.Login_com import *
# from Login.Login_status import *
import socket
from Main import Main_UI

id_input, pw_input, w, con, cur = None, None, None, None, None
status_check = 0
# def Login_online(id):
#     global con, cur
#     sql = "update member set status =1 where id ='" + id + "'"
#     result = cur.execute(sql)
#     print(result)
#     con.commit()
    
def Login_member():
# def Login_member(id_input, pw_input):
    global id_input, pw_input, w, con, cur, status_check
#     global w, con, cur, status_check
    
    id = id_input.get()
    pw = pw_input.get()
    print(id)
    print(pw)
    
    con = pymysql.connect(host ='13.209.92.229', user = 'root', password = '1234', db = 'cloud')
    print('DB인증 >> 연결 성공...')
    print(con)
    
    
    cur = con.cursor()
    print(cur)
    
   
    sql = "select id, pw from member where id = ('" + id + "')and pw = ('" + pw + "')"
    
    result = cur.execute(sql)
    print('전송 성공')
#     con.commit()
    
    recode = cur.fetchone()
    print('로그인 정보: ', recode)
  
    
    if recode!= None:
        if id == recode[0]and pw == recode[1]:
#             mac = socket.gethostbyaddr(socket.gethostname())[2][0]
#             sql = "update member set status =1, mac ='" + mac + "' where id ='" + id + "'"
#             cur.execute(sql)
#             con.commit()
            status_check = 1
            login = Button(Main_UI.w, text="로그인", bg="#FFFF8F", fg="black", width = 10, height = 1, font = ("굴림", 12), borderwidth=1, relief = 'flat', overrelief = 'raised')
            print(type(login))
            login.config(text="로그아웃") 
            
#             Login_status_check(id)
#             Login_online(id)
            messagebox.showinfo('로그인 안내', '로그인 되었습니다.')           
#             w.destroy()
            print("로그인...성공적...")
# #             logincall()
#             logincomplete()
        else:
            messagebox.showinfo('로그인 오류', '아이디나 비밀번호가 다릅니다.')
    con.close()
    print('연결해제')
    print("status_check: ", status_check)
    
    

def Login_event():   
    global id_input, pw_input, w
    w = Toplevel()
    w.geometry("350x300+600+400")
    w.title('로그인')
    w.configure(bg="#FFFF8F")
    intro = Label(w, text='로그인\n', font=('굴림', 20, BOLD), fg = 'black', bg="#FFFF8F")
         
    id_text = Label(w, text='아이디 ', font=('굴림', 15, BOLD), fg = 'blue', bg="#FFFF8F")
    pw_text = Label(w, text='비밀번호 ', font=('굴림', 15, BOLD), fg = 'blue', bg="#FFFF8F")
         
    id_input = Entry(w, font=('굴림', 15), fg = 'black', width=10)
    pw_input = Entry(w, font=('굴림', 15), fg = 'black', width=10)

    intro = Label(w, text='로그인\n', font=('굴림', 20, BOLD), fg = 'black', bg="#FFFF8F")
        
    id_text = Label(w, text='아이디 ', font=('굴림', 15, BOLD), fg = 'blue', bg="#FFFF8F")
    pw_text = Label(w, text='비밀번호 ', font=('굴림', 15, BOLD), fg = 'blue', bg="#FFFF8F")
        
    id_input = Entry(w, font=('굴림', 15), fg = 'black', width=10)
    pw_input = Entry(w, font=('굴림', 15), fg = 'black', width=10)
    
    insert = Button(w, text='로그인', font=('굴림', 20), fg = 'black', command=Login_member)
        
    intro.pack()
    id_text.pack()
    id_input.pack()
    pw_text.pack()
    pw_input.pack()
    insert.pack()

    w.mainloop()
    