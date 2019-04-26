'''
Created on 2019. 4. 17.

@author: jeong
'''
from tkinter import *
from PIL import ImageTk
from Reserve import Reserve_UI 
from CommonDB.DB_select_boxoffice import *
from CommonDB.DB_select_poster import *
from Main.DB_insert_movieinfo import *
from CommonDB.image_url_down_onefile import *
import datetime
from datetime import timedelta
# from Login.Login_UI import *
import socket
from Signup.JoinMember import * 
from Review.ReviewBoardUI import *
from Review import ReviewBoardUI
# from Login import Login_UI

login, status_check, insert = None, 0, None

# DB 입출력 기준날짜 설정
today = datetime.date.today() - timedelta(1)
yesterday = today.strftime('%Y%m%d')
selectday = yesterday

# 창이름, DB에서 불러올 영화정보 
w, record, id_input, pw_input = None, None, None, None


# 로그인/로그아웃 버튼 클릭시 실행 이벤트
def Login_member():
    global id_text, pw_text, id_input, pw_input, w, insert, login
#     global w, con, cur, status_check
    
    if login['text']=="로그인":        
        id = id_input.get()
        pw = pw_input.get()
        if id == "":
            messagebox.showinfo('로그인 오류', '아이디를 입력해주세요.')
        elif pw == "":
            messagebox.showinfo('로그인 오류', '비밀번호를 입력해주세요.')
        else:   
            print(id)
            print(pw)
            
            con = pymysql.connect(host ='13.209.92.229', user = 'root', password = '1234', db = 'cloud')
            print('DB인증 >> 연결 성공...')
        
            cur = con.cursor()
            sql = "select id, pw from member where id = ('" + id + "')and pw = ('" + pw + "')"
            result = cur.execute(sql)
            print('전송 성공')
            recode = cur.fetchone()
            print('로그인 정보: ', recode)
          
            
            if recode!= None:
                if id == recode[0] and pw == recode[1]:
                    login.config(text="로그아웃")
                    id_input.config(state='disable')     
                    pw_input.config(state='disable')   
                    messagebox.showinfo('로그인 안내', '로그인 되었습니다.')
#                     img_logout = PhotoImage(file="D:\\Users\\jeong\\Documents\\workspacePython\\MovieSite\\design\\Logout_Button.png").subsample(5) # make sure to add "/" not "\"
                    img_logout = PhotoImage(file="D:\\jjh\\python\\pyworkspace\\MovieSite\\design\\Logout_Button.png").subsample(5) # make sure to add "/" not "\"
                    login.config(image=img_logout)
                    login.image = img_logout
                    print("로그인...성공적...")
      
            else:
                messagebox.showinfo('로그인 오류', '아이디나 비밀번호가 다릅니다.')
            con.close()
            print('연결해제')
            print("status_check: ", status_check)
    
    elif login['text']=="로그아웃":
        login.config(text="로그인")
        id_input.config(state='normal')     
        pw_input.config(state='normal')
#         img_login = PhotoImage(file="D:\\Users\\jeong\\Documents\\workspacePython\\MovieSite\\design\\Login_Button.png").subsample(5) # make sure to add "/" not "\"
        img_login = PhotoImage(file="D:\\jjh\\python\\pyworkspace\\MovieSite\\design\\Login_Button.png").subsample(5) # make sure to add "/" not "\"
        login.config(image=img_login)
        login.image = img_login
        id_input.delete(0,END)  
        pw_input.delete(0,END)
        messagebox.showinfo('로그아웃 안내', '로그아웃 되었습니다.')
#         status=0
        

# 로그인 영역
def login_area():
    global w, id_text, pw_text, id_input, pw_input
    intro = Label(w, text='로그인\n', font=('굴림', 20, "bold"), fg = 'black', bg="#FFFF8F")
         
    id_text = Label(w, text='아이디 ', font=('굴림', 15, "bold"), fg = 'blue', bg="#FFFF8F")
    pw_text = Label(w, text='비밀번호 ', font=('굴림', 15, "bold"), fg = 'blue', bg="#FFFF8F")
         
    id_input = Entry(w, font=('굴림', 15), fg = 'black', width=13)
    pw_input = Entry(w, font=('굴림', 15), fg = 'black', width=13, show="●")

    id_input.place(x=1130, y=50)
    pw_input.place(x=1130, y=100)


# 예매하기 클릭시 이벤트
def endCall():
    global w
    if login['text']=="로그인":
        messagebox.showinfo('안내', '로그인이 필요합니다.')
    else:
        w.destroy()
        Reserve_UI.call()
        
def ReviewCall():
    global w
    if login['text']=="로그인":
        messagebox.showinfo('안내', '로그인이 필요합니다.')
    else:
        w.destroy()
        ReviewBoardUI.Review_board_call()
    
   
   
# 메인화면
def recall():
    global w, selectday, record, login
    w = Tk()
    w.geometry("1500x800+170+130") # 윈도우 크기 설정
    w.title("영화 프로그램 메인화면") # 윈도우 제목 설정
    w.resizable(width=False, height=False) # 크기고정
    w.configure(bg= "#EBC50A")
    w.attributes('-topmost',False)
    wall = PhotoImage(file = "D:\\jjh\\python\\pyworkspace\\MovieSite\\design\\main_ui.png") 
#     wall = PhotoImage(file = "D:\\Users\\jeong\\Documents\\workspacePython\\MovieSite\\design\\main_ui.png")    
    wall_label = Label(image = wall) 
    wall_label.place(x = -2,y = -2)

    login_area()
    
    # 일간박스오피스 포스터 목록 받아오기
    def read_poster(record):
        for info in record:        
            poster_url = db_process_select_poster(info[0])
            poster_name= poster_down_resize(poster_url)
    
   # 시작시 DB불러오기, DB에 기준날짜의 영화정보가 없으면 API로 DB에 정보 입력
    def read_DB(selectday):
        global record
        try:
            record = db_process_select(selectday)
            read_poster(record)
        except:
            import_totalinfo()   
            record = db_process_select(selectday)
            read_poster(record)

    read_DB(selectday)  
    

    # 메뉴버튼
    review = Button(w, text="영화 리뷰게시판", width = 250, height =50, font = ("굴림", 25),relief = 'raised', overrelief = 'solid',command=ReviewCall,  bg="#FFE400", fg="black") # 리뷰게시판 버튼
#     img_review = PhotoImage(file="D:\\Users\\jeong\\Documents\\workspacePython\\MovieSite\\design\\Review_Button.png").subsample(2) # make sure to add "/" not "\"
    img_review = PhotoImage(file="D:\\jjh\\python\\pyworkspace\\MovieSite\\design\\Review_Button.png").subsample(2) # make sure to add "/" not "\"
    review.config(image=img_review)
    review.place(x=150, y=40)   
    
    reserve = Button(w, text="예매하기", width = 250, height = 50, font = ("굴림", 25),relief = 'raised', overrelief = 'solid', command=endCall,   bg="#FFE400", fg="black") # 영화예매 버튼
#     img_reserve = PhotoImage(file="D:\\Users\\jeong\\Documents\\workspacePython\\MovieSite\\design\\Reserve_Button.png").subsample(2) # make sure to add "/" not "\"
    img_reserve = PhotoImage(file="D:\\jjh\\python\\pyworkspace\\MovieSite\\design\\Reserve_Button.png").subsample(2) # make sure to add "/" not "\"
    reserve.config(image=img_reserve)
    reserve.place(x=500, y=40)   
    
    login = Button(w, text="로그인", bg="#6799FF", fg="white", width = 100, height = 27, font = ("굴림", 12, "bold"), borderwidth=1, relief = 'raised', overrelief = 'solid', command=Login_member) # 로그인 버튼
#     img_login = PhotoImage(file="D:\\Users\\jeong\\Documents\\workspacePython\\MovieSite\\design\\Login_Button.png").subsample(5) # make sure to add "/" not "\"
    img_login = PhotoImage(file="D:\\jjh\\python\\pyworkspace\\MovieSite\\design\\Login_Button.png").subsample(5) # make sure to add "/" not "\"
    login.config(image=img_login)
    login.place(x=1300, y=47)   
    
    signup = Button(w, text="회원가입", bg="#FFFF8F", fg="#6B6B6B", width = 100, height = 27, font = ("굴림", 12, "bold"), borderwidth=1, relief = 'raised', overrelief = 'solid', command=member_insert) # 회원가입 버튼
#     img_signup = PhotoImage(file="D:\\Users\\jeong\\Documents\\workspacePython\\MovieSite\\design\\Signup_Button.png").subsample(5) # make sure to add "/" not "\"
    img_signup = PhotoImage(file="D:\\jjh\\python\\pyworkspace\\MovieSite\\design\\Signup_Button.png").subsample(5) # make sure to add "/" not "\"
    signup.config(image=img_signup)
    signup.place(x=1300, y=97)   
       
    
    # 인기영화 타이틀
#     hotranktitle = Label(w, text="Today's Hot Movie!!!", font=("굴림", 25), fg="red", bg="#FFFF8F") # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
#     hotranktitle.place(x=300, y=170)
#     hotrank1 = Label(w, text="1위", font=("굴림", 20), fg="black", bg="#FFFF8F") # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
#     hotrank1.place(x=150, y=270)
#     hotrank2 = Label(w, text="2위", font=("굴림", 20), fg="black", bg="#FFFF8F") # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
#     hotrank2.place(x=430, y=270)
#     hotrank3 = Label(w, text="3위", font=("굴림", 20), fg="black", bg="#FFFF8F") # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
#     hotrank3.place(x=710, y=270)
   
    # 인기영화 포스터
    def hotrank(record):
        
        rank1 = record[0][2][49:66]
        rank2 = record[1][2][49:66]
        rank3 = record[2][2][49:66]
        
        icon1 = ImageTk.PhotoImage(file = u'D:\jjh\python\pyworkspace\MovieSite\Poster\%s.jpg' % rank1) # 변수에 이미지 저장
#         icon1 = ImageTk.PhotoImage(file = 'D:\\Users\\jeong\\Documents\\workspacePython\\MovieSite\\Poster\\%s.jpg' % rank1) # 변수에 이미지 저장
        hotrank1_img = Label(w) # Label에 이미지변수 할당
        hotrank1_img.configure(image=icon1)
        hotrank1_img.image = icon1    
        hotrank1_img.place(x=75, y = 410)
        
        icon2 = ImageTk.PhotoImage(file = u'D:\jjh\python\pyworkspace\MovieSite\Poster\%s.jpg' % rank2) # 변수에 이미지 저장
#         icon2 = ImageTk.PhotoImage(file = 'D:\\Users\\jeong\\Documents\\workspacePython\\MovieSite\\Poster\\%s.jpg' % rank2) # 변수에 이미지 저장
        hotrank2_img = Label(w) # Label에 이미지변수 할당
        hotrank2_img.configure(image=icon2)
        hotrank2_img.image = icon2   
        hotrank2_img.place(x=355, y = 410)
        
        icon3 = ImageTk.PhotoImage(file = u'D:\jjh\python\pyworkspace\MovieSite\Poster\%s.jpg' % rank3) # 변수에 이미지 저장
#         icon3 = ImageTk.PhotoImage(file = 'D:\\Users\\jeong\\Documents\\workspacePython\\MovieSite\\Poster\\%s.jpg' % rank3) # 변수에 이미지 저장
        hotrank3_img = Label(w) # Label에 이미지변수 할당
        hotrank3_img.configure(image=icon3)
        hotrank3_img.image = icon3
        hotrank3_img.place(x=635, y = 410)
    
    
    
    
    
    # 박스오피스    
#     boxofficetitle = Label(w, text="Box Office", font=("굴림", 25), fg="red", bg="#FFFF8F") # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
#     boxofficetitle.place(x=1090, y=170)
    boxofficesubtitle = Label(w, text="순위\t        영화명\t        누적관객수", font=("배달의민족 한나는 열한살", 17, "bold"), fg="black", bg="#FFFF8F") # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
#     boxofficesubtitle.place(x=970, y=240)
    
    frame_box=Frame(w, bd=8, width = 500, height=400, relief='groove', bg="#FFFF8F", padx=20, pady=10)
    frame_box.place(x=935,y=280)
 
    
    
    
    
    
    rank=[1,2,3,4,5,6,7,8,9,10]
        
    def boxoffice_ui(record):
    
        start = 1   # row를 증가시켜주는 변수
        
        for result in record:        
            rank_input = Label(frame_box, text=rank[start-1],bg ="#FFFF8F",fg="black",font =("배달의민족 한나는 열한살",17), padx=17, pady=7) # 출력칸 정의
            title_input = Label(frame_box, text=result[0],bg ="#FFFF8F",fg="black",font =("배달의민족 한나는 열한살",17), padx=55, pady=7) # 출력칸 정의
            people_input = Label(frame_box, text=result[1],bg ="#FFFF8F",fg="black",font =("배달의민족 한나는 열한살",17), padx=1) # 출력칸 정의
            
    
            rank_input.grid(row = start, column=0) # 출력칸 윈도우에 삽입    
            title_input.grid(row = start, column=1) # 출력칸 윈도우에 삽입    
            people_input.grid(row = start, column=2, sticky='e', padx=10) # 출력칸 윈도우에 삽입          
        
            start += 1
    

    boxoffice_ui(record)
    hotrank(record)
    
    w.mainloop()

if __name__ == '__main__':
    recall()
