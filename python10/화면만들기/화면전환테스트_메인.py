'''
Created on 2019. 4. 17.

@author: user
'''
from tkinter import *
from 화면만들기 import 화면전환테스트_호출

w = None

def endCall():
    global w
    w.destroy()
    화면전환테스트_호출.call()
    
def recall():
    global w
    w = Tk()
    b = Button(w, text="호출모듈로 가요.", command=endCall)
    b.pack()
    w.mainloop()

if __name__ == '__main__':
    recall()