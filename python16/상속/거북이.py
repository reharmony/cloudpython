import turtle
import random

colorlist = ['red', 'yellow', 'green', 'blue', 'black']

def leftClick(x,y):
    print('x축:', x, ", ", 'y축:', y)

    color = random.choice(colorlist)

    myTurtle.pencolor(color)
    myTurtle.goto(x,y)

    # width = 50
    # height = 50
    # sx1 = x - width
    # sy1 = y - height
    # myTurtle.goto(sx1,sy1)
    # sx1 = x - width/2
    # myTurtle.penup() # 펜 떼고 이동만
    # myTurtle.goto(200,200)
    # myTurtle.pendown() # 펜 데고 그리면서 이동
    # myTurtle.goto(x,y)

myTurtle = turtle.Turtle('turtle')
turtle.title('거북이로 그림을 그려요.')
myTurtle.pensize(20)
myTurtle.pencolor('red')
turtle.onscreenclick(leftClick,1)
# turtle.onscreenwheel(leftClick,1)
turtle.done()
