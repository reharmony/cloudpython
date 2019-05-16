from tkinter import *

top = Tk()


frame = Frame(top)
frame.pack(fill=BOTH)

xscrollbar = Scrollbar(frame, orient=HORIZONTAL)
xscrollbar.grid(row=1, column=0, sticky=E+W)

yscrollbar = Scrollbar(frame)
yscrollbar.grid(row=0, column=1, sticky=N+S)

canvas = Canvas(frame, bd=0,scrollregion=(0, 0, 500, 500), xscrollcommand=xscrollbar.set,yscrollcommand=yscrollbar.set)
canvas.grid(row=0, column=0, sticky=N+S+E+W)


canvas.create_rectangle(250, 250, 400, 400, fill="blue")

xscrollbar.config(command=canvas.xview)
yscrollbar.config(command=canvas.yview)

top.mainloop()