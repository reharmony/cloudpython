'''
Created on 2019. 5. 1.

@author: user
'''
### 하루의 일과를 나타내는 프로그램 ###

class Day:
    what = '';
    time = '';
    location = '';
    
    def __init__(self, what, time, location):
        self.what = what
        self.time = time
        self.location = location       
    
    def __str__(self):
        return self.what + ", %d" % self.time + ", " + self.location

day1 = Day('밥',30,'w몰')
day2 = Day('파이썬공부',120,'KG학원')
day3 = Day('운동', 60, '공원')

days=[]
days.append(day1)
days.append(day2)
days.append(day3)

print("전체 하는 일의 시간은:", day1.time + day2.time + day3.time)
print("평균 하는 일의 시간은:", (day1.time + day2.time + day3.time)/3)
print("매일 무엇을 얼마나 어디에서 했는가:", day1, "/", day2, "/",  day3)
print("며칠 간 했는지:", len(days) )
