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
    end["text"] = "계산결과는 " + str(result)

def onClick2():
    data1 = int(num1_in.get())
    data2 = int(num2_in.get())
    result = data1 - data2
    end["text"] = "계산결과는 " + str(result)

def onClick3():
    data1 = int(num1_in.get())
    data2 = int(num2_in.get())
    result = data1 * data2
    end["text"] = "계산결과는 " + str(result)
    
def onClick4():
    data1 = int(num1_in.get())
    data2 = int(num2_in.get())
    result = data1 / data2
    end["text"] = "계산결과는 " + str(result)
    
w = Tk()
w.title("미니 계산기")
w.geometry("240x150-900-500")
f1=Frame(w)
f1.pack(side="top")
f2=Frame(w)
f2.pack(side="bottom")

# 숫자 입력1
num1 = Label(f1, text = "첫번째 숫자를 입력하세요.")
num1.pack()

num1_in = Entry(f1)
num1_in.pack()

# 숫자 입력2
num2 = Label(f1, text = "두번째 숫자를 입력하세요.")
num2.pack()

num2_in = Entry(f1)
num2_in.pack()

# 버튼 4개 만들기
plus = Button(f1, text ="+", command = onClick1, width = 5)
plus.pack(side = "left", padx=7,pady=10)

minus = Button(f1, text ="-", command = onClick2, width = 5)
minus.pack(side = "left", padx=7)

mul = Button(f1, text ="*", command = onClick3, width = 5)
mul.pack(side = "left", padx=7)

div = Button(f1, text ="/", command = onClick4, width = 5)
div.pack(side = "left", padx=7)

# 결과 출력창

end = Label(f2, text = "여기에 계산 결과 출력")
end.pack(pady=5)

w = mainloop()

