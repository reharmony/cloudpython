'''
Created on 2019. 4. 17.

@author: user
'''
from tkinter import *
from urllib import request
from bs4 import BeautifulSoup

def saveFile():
    target = request.urlopen("http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
    soup = BeautifulSoup(target, "html.parser")
    result = soup.select("location")
    print(result)
    print(type(result))
    print(len(result))
    
    for location in result:
        city = location.select_one("city").string
        wf = location.select_one("wf").string
        tmn = location.select_one("tmn").string
        tmx = location.select_one("tmx").string
        print(city, wf, tmn, tmx)
        
        saveFile = open(city + ".txt", "w")
        saveFile.write(city + "\n")
        saveFile.write(wf + "\n")
        saveFile.write(tmn + "\n")
        saveFile.write(tmx + "\n")
        
        saveFile.close()

input
def readFile():
    global input
    input = input("날씨 예보를 알고 싶은 도시명을 입력하세요.>> ")
    readFile = open(input + ".txt", "r")
    contents = readFile.read()
    text.insert(END, contents)


w= Tk()
w.geometry("400x400")

intro = Label(w, text="날씨 정보를 읽어오겠습니다.", fg="blue", bg="pink", font="궁서 20 bold")
save = Button(w, text="웹사이트 크롤링 파일로 저장", fg="blue", bg="yellow", font="궁서 20 bold", command=saveFile)
read = Button(w, text="날씨 정보 파일로부터 읽기", fg="blue", bg="yellowgreen", font="궁서 20 bold", command=readFile)
text = Text(w, height=10, width=40,fg="black", bg="skyblue", font="궁서 20 bold")





intro.pack()
save.pack()
read.pack()
text.pack()




w.mainloop()