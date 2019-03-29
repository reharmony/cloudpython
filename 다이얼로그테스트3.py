from tkinter import *

def onClick():
    data1 = name_t.get()
    print("입력한 이름은 %s입니다." % data1)
    data2 = int(year_t.get())
    age = 2019 - data2 + 1
    print("현재 나이는 %d세 입니다." % age)
    result["text"] = "나이는" + str(age) 
    
w = Tk()



# 1. 이름입력(라벨, 입력란 필요)
name = Label(w, text = "이름을 입력하세요.")
name.pack()

name_t = Entry(w)
name_t.pack()

# 2. 태어난 해를 입력
year = Label(w, text = "태어난 해를 입력하세요.")
year.pack()

year_t = Entry(w)
year_t.pack()

# 3. 버튼 처리

btn = Button(w, text = "입력하기", command = onClick)
btn.pack()

result = Label(w, text = "여기에 나이 출력" )
result.pack()

w.mainloop()