list = [1,5,8,2,3,9,7]

for x in range(0,len(list)):
    min = list[0]
    if min > list[x]:
        min = list[x]
        
print("최소값은", min)

print("------------")

