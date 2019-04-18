'''
Created on 2019. 4. 14.

@author: jeong
'''
import threading
def ToDo():
    print("Timer")
    timer = threading.Timer(10, ToDo)
    timer.start()
  
if __name__ == '__main__':
    ToDo()