'''
Created on 2019. 4. 17.

@author: user
'''
from tkinter import *
from 영화사이트화면구성 import 예매화면

w = None

def endCall():
    global w
    w.destroy()
    예매화면.call()
    
def recall():
    global w
    w = Tk()
    w.geometry("1500x800+100+100") # 윈도우 크기 설정
    w.title("영화사이트 메인화면") # 윈도우 제목 설정
    w.resizable(width=False, height=False) # 크기고정
    w.configure(bg="white")
    
    # 메뉴버튼
    review = Button(w, text="영화 리뷰게시판", width = 17, height =1, font = ("굴림", 25),relief = 'groove', overrelief = 'solid',command=endCall) # 영화예매 버튼
    review.place(x=50, y=30)   
    reserve = Button(w, text="영화 예매", width = 17, height = 1, font = ("굴림", 25),relief = 'groove', overrelief = 'solid', command=endCall) # 영화예매 버튼
    reserve.place(x=500, y=30)   
    login = Button(w, text="로그인", bg="white", width = 10, height = 1, font = ("굴림", 12), borderwidth=1, relief = 'flat', overrelief = 'raised', command=endCall) # 영화예매 버튼
    login.place(x=1000, y=45)   
    singup = Button(w, text="회원가입", bg="white", width = 10, height = 1, font = ("굴림", 12), borderwidth=1, relief = 'flat', overrelief = 'raised', command=endCall) # 영화예매 버튼
    singup.place(x=1200, y=45)   
    
    # 인기영화 타이틀
    hotranktitle = Label(w, text="Today's Hot Movie!!!", font=("굴림", 25), fg="red", bg="white") # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
    hotranktitle.place(x=300, y=170)
    hotrank1 = Label(w, text="1위", font=("굴림", 20), fg="black", bg="white") # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
    hotrank1.place(x=150, y=270)
    hotrank2 = Label(w, text="2위", font=("굴림", 20), fg="black", bg="white") # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
    hotrank2.place(x=430, y=270)
    hotrank3 = Label(w, text="3위", font=("굴림", 20), fg="black", bg="white") # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
    hotrank3.place(x=710, y=270)
    
    # 인기영화 포스터
    icon1 = PhotoImage(file = 'm1.png') # 변수에 이미지 저장
    hotrank1_img = Label(w) # Label에 이미지변수 할당
    hotrank1_img.configure(image=icon1)
    hotrank1_img.image = icon1    
    hotrank1_img.place(x=75, y = 330)
    
    icon2 = PhotoImage(file = 'm2.png') # 변수에 이미지 저장
    hotrank2_img = Label(w) # Label에 이미지변수 할당
    hotrank2_img.configure(image=icon2)
    hotrank2_img.image = icon2   
    hotrank2_img.place(x=355, y = 330)
    
    icon3 = PhotoImage(file = 'm3.png') # 변수에 이미지 저장
    hotrank3_img = Label(w) # Label에 이미지변수 할당
    hotrank3_img.configure(image=icon3)
    hotrank3_img.image = icon3
    hotrank3_img.place(x=635, y = 330)
    
    # 박스오피스    
    boxofficetitle = Label(w, text="Box Office", font=("굴림", 25), fg="red", bg="white") # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
    boxofficetitle.place(x=1100, y=170)
    boxofficesubtitle = Label(w, text="1\t영화제목\t\t누적관객수", font=("굴림", 15), fg="black", bg="white") # 레이블 정의 (부모 윈도우, 출력할 텍스트, 속성값)
    boxofficesubtitle.place(x=1000, y=250)
    
    
    
    w.mainloop()

if __name__ == '__main__':
    recall()