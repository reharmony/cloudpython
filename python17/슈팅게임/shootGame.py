import pygame
import random
import sys

## 전역 변수 ##
monitor = None
r, g, b = [0] * 3
swidth, sheight = 500, 700
ship = None # 우주선 변수 초기화
shipSize = 0
montser = None # 우주괴물 변수 초기화
missile = None # 미사일 변수 초기화
fireCount = 0 # 미사일 명중 카운터 초기화
monster_state = 0 # 몬스터 상태, 1이면 명중됨

# 우주괴물 이미지 파일 리스트
monsterImage = ['monster01.png','monster02.png',\
                'monster03.png','monster04.png',\
                'monster05.png','monster06.png',\
                'monster07.png','monster08.png',\
                'monster09.png','monster10.png',]

# 개체를 화면에 그려주는 함수
def paintEntity(entity, x, y):
    monitor.blit(entity, (x,y))

def writeScore(fireCount):
    myfont = pygame.font.Font('NanumGothic.ttf', 20)
    txt = myfont.render(u'파괴한 우주괴물 수 : ' +  str(fireCount), True, (255-r, 255-g, 255-b))
    monitor.blit(txt, (10, sheight - 40))

# 게임 실행시 동작 함수
def playGame():
    global monitor, ship, monster, missile, fireCount, monster_state
    r = random.randrange(0,255)
    g = random.randrange(0,255)
    b = random.randrange(0,255)

    # X,Y 좌표값은 창의 좌상단 기준 (0,0)
    shipX = swidth / 2 # 우주선 최초 위치 X축
    shipY = sheight * 0.8 # 우주선 최초 위치 Y축
    dx, dy = 0, 0 # 방향키 눌렀을 때 이동값

    # 우주괴물
    monster = pygame.image.load(random.choice(monsterImage)) # 이미지 무작위 선택
    monsterSize = monster.get_rect().size # 이미지 크기 알아오기
    monsterX = 0
    monsterY = random.randrange(0,int(swidth * 0.3))
    monsterSpeed = random.randrange(1,5)

    missileX, missileY = None, None # 미사일 위치 초기화

    count = 1 # 업데이트 카운터 초기화
    monster_state = 0

    while True:
        # 업데이트 주기 (작을수록 느려짐)
        (pygame.time.Clock()).tick(50)

        # 배경색 채우기
        monitor.fill((r, g, b))

        # 키보드나 마우스 이벤트 체크
        for e in pygame.event.get():
            if e.type in [pygame.QUIT]: # X버튼 클릭시 이벤트 [종료]
                pygame.quit()
                sys.exit()

            # 방향키 이벤트 처리
            if e.type in [pygame.KEYDOWN]:
                if e.key == pygame.K_LEFT:
                    dx = -5
                elif e.key == pygame.K_RIGHT:
                    dx = +5
                elif e.key == pygame.K_UP:
                    dy = -5
                elif e.key == pygame.K_DOWN:
                    dy = +5
                elif e.key == pygame.K_SPACE:
                    if missileX == None:
                        missileX = shipSize[0] / 2 + shipX
                        missileY = shipY

            # 방향키 떼면 우주선이 멈춘다
            if e.type in [pygame.KEYUP]:
                if e.key == pygame.K_LEFT or \
                   e.key == pygame.K_RIGHT or \
                   e.key == pygame.K_UP or \
                   e.key == pygame.K_DOWN:
                    dx, dy = 0, 0

        # 우주선이 화면 안에서만 움직이게 한다
        if (0 < shipX + dx and shipX + dx <= swidth - shipSize[0]) \
                and (sheight / 2 < shipY + dy and shipY + dy <= sheight - shipSize[1]):
            shipX += dx
            shipY += dy

        paintEntity(ship, shipX, shipY) # 우주선 화면에 배치

        # 우주괴물 이동
        monsterX += monsterSpeed
        if monsterX > swidth :
            monsterX = 0
            monsterY = random.randrange(0,int(swidth * 0.3))
            monster = pygame.image.load(random.choice(monsterImage))
            monsterSize = monster.get_rect().size
            monsterSpeed = random.randrange(1,5)

        paintEntity(monster, monsterX, monsterY)  # 우주괴물 화면에 배치

        if missileX != None: # 미사일 발사하면 위로 계속 올라감
            missileY -= 10
            if missileY < 0: # 미사일에 맨 위에 도달하면 사라짐
                missileX, missileY = None, None
        if missileX != None: # 미사일 화면에 배치
            paintEntity(missile,missileX,missileY)

            # 미사일 맞았는지 체크
            if (monsterX < missileX and missileX < monsterX + monsterSize[0]) and \
                    (monsterY < missileY and missileY < monsterY + monsterSize[1]) :
                fireCount += 1 # 미사일 명중 카운트 증가

                # 우주괴물 새로 불러오기
                monster = pygame.image.load(random.choice(monsterImage))  # 이미지 무작위 선택
                monsterSize = monster.get_rect().size  # 이미지 크기 알아오기
                monsterX = 0
                monsterY = random.randrange(0, int(swidth * 0.3))
                monsterSpeed = random.randrange(1, 5)

                # monster = pygame.image.load('boom_70.png')

                # monster_state = 1

        writeScore(fireCount)

        # 화면 업데이트
        pygame.display.update()

        # 업데이트 카운터
        print('update 횟수:',count)
        count += 1

        # if monster_state == 0:
        #     # 화면 업데이트
        #     pygame.display.update()
        #
        #     # 업데이트 카운터
        #     print('update 횟수:',count)
        #     count += 1
        #
        # if monster_state == 1:
        #     # 우주괴물 새로 불러오기
        #     monster = pygame.image.load(random.choice(monsterImage))  # 이미지 무작위 선택
        #     monsterSize = monster.get_rect().size  # 이미지 크기 알아오기
        #     monsterX = 0
        #     monsterY = random.randrange(0, int(swidth * 0.3))
        #     monsterSpeed = random.randrange(1, 5)
        #
        #     pygame.display.update()
        #
        #     # 업데이트 카운터
        #     print('update 횟수:', count)
        #     count += 1


## 메인 코드 ##

pygame.init() # 파이게임 기능 시작
pygame.display.set_caption('미니 갤러그') # 창 제목
monitor = pygame.display.set_mode((swidth,sheight)) # tkinter에서 w와 같은 것

ship = pygame.image.load('ship02.png') # 내 우주선 이미지 파일 로드
shipSize = ship.get_rect().size # 이미지 크기 알아오기

missile = pygame.image.load('missile.png') # 미사일 이미지 파일 로드

playGame() # 게임 실행



