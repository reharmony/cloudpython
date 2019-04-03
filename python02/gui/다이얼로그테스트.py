# tkinter : 라이브러리의 한 종류 (파이썬 기본 내장 라이브러리)
from tkinter import *
from tkinter import messagebox


# 함수 정의하기: def 함수명():
def onClick():
    # *.get()은 input의 기능
    data1 = text.get()
    messagebox.showinfo("입력받은 값>> ", data1)
    print("입력받은값>> ", data1)

# 파란색 !표 뜨는 메시지 박스
messagebox.showinfo("창 제목입니다.", "창 내용입니다.")

# 틀(창) 만들기 => 틀변수이름 = Tk()
root = Tk()

# 창내용 입력: 레이블변수이름 = Lable(틀변수, 속성 = "창에 출력할 내용", command = 호출할 함수)
name = Label(root, text = "이름을 입력하세요.")
# pack : 위에서 정의한 내용을 실제로 창에 얹기
name.pack()

# 입력칸 추가: 입력칸변수이름 = Entry(틀변수)
text = Entry(root)
text.pack()

# 버튼변수이름.Button(변수, 속성 = "버튼에 출력할 내용")
btn = Button(root, text = "입력",command = onClick)
btn.pack()

# 창 계속 유지하기 
root.mainloop()


 
