import turtle
import random

# 좌클릭시 이벤트
def leftClick(x,y):
    print('x축:', x, ", ", 'y축:', y)

    # 펜 사이즈
    size = random.randrange(1, 20)
    myTurtle.pensize(size)

    # 펜 색상
    r = random.random()
    g = random.random()
    b = random.random()
    myTurtle.pencolor(r,g,b)

    # 사격형 시작 좌표 범위
    rand_x = random.randrange(-400,400)
    rand_y = random.randrange(-400,400)

    # 사격형 좌우길이 및 상하길이
    width = random.randrange(50,300)
    height = random.randrange(50,300)

    # 그리기 시작 위치 계산
    sx1 = rand_x - width/2
    sy1 = rand_y - height/2

    # 자리 초기화
    myTurtle.penup() # 펜 떼고 이동만
    myTurtle.goto(sx1,sy1)

    # 좌변
    sy2 = sy1 + height
    myTurtle.pendown() # 그리면서 이동
    myTurtle.goto(sx1,sy2)

    # 상변
    sx2 = sx1 + width
    myTurtle.goto(sx2,sy2)

    # 우변
    myTurtle.goto(sx2,sy1)

    # 하변
    myTurtle.goto(sx1,sy1)

myTurtle = turtle.Turtle('turtle')
turtle.title('거북이로 그림을 그려요.')
turtle.onscreenclick(leftClick,1)
turtle.done()
