#### 미니 계산기 만들기 ####
# 두 수를 입력받고
# 버튼을 4개 만들어서 (+,-,*,/)
# 맨 아래에 계산 결과 출력하기 

from tkinter import *
from tkinter import messagebox


# 함수정의
def onClick1():
    data1 = int(num1_in.get())
    data2 = int(num2_in.get())
    result = data1 + data2
    end["text"] = "계산결과는" + str(result)

def onClick2():
    data1 = int(num1_in.get())
    data2 = int(num2_in.get())
    result = data1 - data2
    end["text"] = "계산결과는" + str(result)

def onClick3():
    data1 = int(num1_in.get())
    data2 = int(num2_in.get())
    result = data1 * data2
    end["text"] = "계산결과는" + str(result)
    
def onClick4():
    data1 = int(num1_in.get())
    data2 = int(num2_in.get())
    result = data1 / data2
    end["text"] = "계산결과는" + str(result)
    
w = Tk()
w.title("미니 계산기")
w.geometry("240x200-900-500")


# 숫자 입력1
num1 = Label(w, text = "첫번째 숫자를 입력하세요.")
num1.pack()

num1_in = Entry(w)
num1_in.pack()

# 숫자 입력2
num2 = Label(w, text = "두번째 숫자를 입력하세요.")
num2.pack()

num2_in = Entry(w)
num2_in.pack()

# 버튼 4개 만들기
plus = Button(w, text ="+", command = onClick1, width = 5)
plus.pack(side = "left", padx=7, pady=1)

minus = Button(w, text ="-", command = onClick2, width = 5)
minus.pack(side = "left", padx=7, pady=1)

mul = Button(w, text ="*", command = onClick3, width = 5)
mul.pack(side = "left", padx=7, pady=1)

div = Button(w, text ="/", command = onClick4, width = 5)
div.pack(side = "left", padx=7, pady=1)

# 결과 출력창
f2=Frame()
end = Label(w, text = "여기에 계산 결과 출력")
end.pack(padx=7, pady=100)

w = mainloop()

