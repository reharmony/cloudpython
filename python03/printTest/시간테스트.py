import datetime
import time

now = datetime.datetime.now()
print(now)
print("----------")

time.sleep(5) # 재워요!!
print(now.year)
print(now.month)
print(now.day)
print(now.weekday()) # 0 = 월요일
print('월화수목금토일'[now.weekday()]) # 0 = 월요일
print(now.hour)
print(now.minute)
print(now.second)

