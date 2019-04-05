import operator

# 기차 목록
train_tup=[('토마스',5),('헨리',8),('에드워드',9),
           ('에밀리',6),('퍼시',5),('고든',13)]

print("기차 수속량 목록:",train_tup)

print("")

# 제목
print("-------------------------")
print("기차\t수송량\t순위")
print("-------------------------")

train_rank = sorted(train_tup, key=operator.itemgetter(1), reverse=True)

rank = 1

# 이름, 수송량, 순위 출력
for x in range(0,len(train_rank)):
    for y in range(0,len(train_rank[0])):
        print(train_rank[x][y], end="\t")
    if train_rank[x][1] < train_rank[x-1][1]:
        rank +=1    
    print(rank,"위")

print("-------------------------")

