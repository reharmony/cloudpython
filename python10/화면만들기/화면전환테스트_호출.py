'''
Created on 2019. 4. 17.

@author: user
'''
from tkinter import *
from 화면만들기 import 화면전환테스트_메인

w2 = None

def endCall2():
    global w2
    w2.destroy()
    화면전환테스트_메인.recall()
    
def call():
    global w2
    w2 = Tk()
    b = Button(w2, text="메인으로 다시 돌아가요.", command=endCall2)
    b.pack()
    w2.mainloop()
