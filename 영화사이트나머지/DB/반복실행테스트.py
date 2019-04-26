'''
Created on 2019. 4. 14.

@author: jeong
'''
import sched, time

s = sched.scheduler(time.time, time.sleep)
def do_something(sc): 
    print("반복실행...")
    s.enter(3, 1, do_something, (sc,))

s.enter(3, 1, do_something, (s,))
s.run()


