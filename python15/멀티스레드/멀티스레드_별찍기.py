import threading
import time


class Print:
    shape = ''

    def __init__(self, shape):
        self.shape = shape

    def show(self):
        for _ in range (0,50):
            print(self.shape)
            time.sleep(0.2)

shape1 = Print('★')
shape2 = Print('■')
shape3 = Print('☎')

t1 = threading.Thread(target = shape1.show)
t2 = threading.Thread(target = shape2.show)
t3 = threading.Thread(target = shape3.show)

t1.start()
t2.start()
t3.start()