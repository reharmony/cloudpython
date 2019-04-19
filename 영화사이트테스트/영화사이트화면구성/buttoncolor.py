# -*- coding:utf-8 -*-

from tkinter import *

 

class MyApp:

    def __init__(self,parent):

        self.myparent=parent

       

        #--- mainframe 생성 ---

        self.mainframe=Frame(self.myparent)

        self.mainframe.pack()

 

        #--- button1 생성 ---

        self.button1=Button(self.mainframe,

                            text="OK",

                            bg="green",

                            command=self.button1click) #명령어묶기로 메서드를 지정

        self.button1.pack()

       

    #button1의 command에 사용된 함수

    def button1click(self):

        if self.button1['bg']=='green':

            self.button1['bg']='yellow'

        else:

            self.button1['bg']='green'

 

root=Tk()

myapp=MyApp(root)

root.mainloop()