import turtle
import random

class Shape:
    myTurtle = None # 거북이 변수
    cx, cy = 0, 0 # 도형 중심

    def __init__(self):
        self.myTurtle = turtle.Turtle('turtle') # 거북이 생성

    # 펜 색상
    def setPen(self):
        r = random.random()
        g = random.random()
        b = random.random()
        self.myTurtle.pencolor((r,g,b))
        pSize = random.randrange(1,10)
        self.myTurtle.pensize(pSize)

    # 상속할 함수
    def drawShape(self):
        pass

# 사각형 그리기
class Rectangle(Shape):
    width, height = [0] * 2

    def __init__(self,x,y):
        Shape.__init__(self)
        self.cx = x
        self.cy = y
        # 길이 및 높이 설정
        self.width = random.randrange(20,100)
        self.height = random.randrange(20,100)

    # 그리기
    def drawShape(self):
        sx1, sy1, sx2, sy2 = [0] * 4

        sx1 = self.cx - self.width/2
        sy1 = self.cy - self.width/2
        sx2 = self.cx + self.width/2
        sy2 = self.cy + self.width/2

        self.setPen()
        self.myTurtle.penup()
        self.myTurtle.goto(sx1,sy1)
        self.myTurtle.pendown()

        self.myTurtle.goto(sx1,sy2)
        self.myTurtle.goto(sx2,sy2)
        self.myTurtle.goto(sx2,sy1)
        self.myTurtle.goto(sx1,sy1)

# 별 그리기
class Stars(Shape):

    def __init__(self):
        Shape.__init__(self)

    # 그리기
    def drawShape(self, x, y):
        self.setPen()
        self.myTurtle.penup()
        self.myTurtle.goto(x,y)
        self.myTurtle.pendown()

        for i in range(0,20):
            self.myTurtle.left(130) # 방향전환 각도
            self.myTurtle.forward(200) # 진행 길이

# 클릭시 실행할 이벤트
def screenLeftClick(x,y):
    select = input('1.사각형 2.별 >> ')
    if select == '1':
        rect = Rectangle(x,y)
        rect.drawShape()

    if select == '2':
        star = Stars()
        star.drawShape(x,y)

# 메인 코드
turtle.title('거북이로 객체지향 사각형 그리기')
turtle.onscreenclick(screenLeftClick, 1)
turtle.done()
