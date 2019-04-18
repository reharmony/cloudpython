'''
Created on 2019. 4. 18.

@author: user
'''
from string import ascii_uppercase

alpha = list(ascii_uppercase)
number = list(range(1,101))

# alphabet
seat_list=[]
for x in range(0,5):
    for y in range(0,5):
        seat_list.append("%s%c%d" % ("seat_",alpha[x], number[y])) 
print(seat_list)


x = 0
seat_all=[]
for y in range(0,5):
    row = 0    
    seat_row=[]
    for i in range(x,x+5):
        seat_row.append(seat_list[i])
        row += 1
    x += 5
    seat_all.append(seat_row)

print(row)
print(seat_all)
