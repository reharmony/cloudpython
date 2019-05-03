import turtle

t = turtle.Pen()

while True:
    방향 = input('왼쪽: left, 오른쪽: right >> ')
    각도 = int(input('각도 입력>> '))
    if 방향 == 'left':
        t.left(각도) # 왼쪽으로 90도 방향 전환
        t.forward(200) # 진행방향으로 쭉 진행

    elif 방향 == 'right':
        t.right(각도)
        t.forward(200) # 진행방향으로 쭉 진행
