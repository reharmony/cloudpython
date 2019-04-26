import datetime
import time

now = datetime.datetime.now()

print("지금 몇 시인가요?")
hour = now.hour
print(hour,"시 ")
 
if hour<=22:
    print("아직 집에 갈 시간이 멀었군요.")
else:
    print("집에 갈 시간이군요.")
    