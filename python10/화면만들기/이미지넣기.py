'''
Created on 2019. 4. 11.

@author: user
'''
from tkinter import *
from tkinter.messagebox import *

label = None

def img_change():
    global label
    w.visilbe = True
    icon2 = PhotoImage(file="m2.png")
    label.configure(image = icon2)
    label.image = icon2

if __name__ == '__main__':
    
    w = Tk()
    icon = PhotoImage(file = "m1.png") # 변수에 이미지 저장
    label = Label(w,image=icon) # Label에 이미지변수 할당
    label.image = icon
    
    button = Button(w, text = "나를 눌러요....", command = img_change) # 버튼에 img_change 함수 할당  
    
    label.pack() # 레이블 삽입
    button.pack() # 버튼 삽입
    
    # showinfo("여기는 제목 부분...", "여기는 출력내용 보이는 곳...")  # 메세지박스(제목, 내용)
    # showinfo("나는 메세지 박스...", "출력은 여기에 보여요...")
    
    w.mainloop()