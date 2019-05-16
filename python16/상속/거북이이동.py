import turtle
import random

colorlist = ['red', 'yellow', 'green', 'blue', 'black']

def leftClick(x,y):
    print('x축:', x, ", ", 'y축:', y)

    myTurtle.penup()

    color = random.choice(colorlist)

    myTurtle.pencolor(color)
    myTurtle.goto(x,y)


myTurtle = turtle.Turtle('turtle')
turtle.title('거북이로 그림을 그려요.')
myTurtle.pensize(20)
myTurtle.pencolor('red')
turtle.onscreenclick(leftClick,1)
# turtle.onscreenwheel(leftClick,1)
turtle.done()
