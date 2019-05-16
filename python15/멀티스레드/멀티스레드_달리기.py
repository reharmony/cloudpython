import threading
import time
import random


class Run:
    shape = ''
    distance = 0

    def __init__(self, shape, distantce):
        self.shape = shape
        self.distance = distantce

    def show(self):
        rand = random.randrange(5, 10)
        for _ in range (0,100):
            self.distance = self.distance + rand
            print(self.shape, self.distance)
            time.sleep(0.2)
            if self.distance >= 95:
                print(self.shape + " 결승선 도착")
                break

shape1 = Run('1번마',0)
shape2 = Run('2번마',0)
shape3 = Run('3번마',0)

t1 = threading.Thread(target = shape1.show)
t2 = threading.Thread(target = shape2.show)
t3 = threading.Thread(target = shape3.show)

t1.start()
t2.start()
t3.start()