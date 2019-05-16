import threading
import time


class RacingCar:
    carName = ''

    def __init__(self, carName):
        self.carName = carName

    def runCar(self):
        for _ in range(0,10):
            carStr = self.carName + '~~ 달립니다.'
            print(carStr)
            time.sleep(0.1)

car1 = RacingCar('appleCar')
car2 = RacingCar('bananaCar')
car3 = RacingCar('melonCar')

car1.runCar()
car2.runCar()
car3.runCar()

print()

t1 = threading.Thread(target = car1.runCar)
t2 = threading.Thread(target = car2.runCar)
t3 = threading.Thread(target = car3.runCar)

t1.start()
t2.start()
t3.start()

