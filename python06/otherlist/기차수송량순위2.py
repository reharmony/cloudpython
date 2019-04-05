import operator

# 기차 목록
train_tup=[('토마스',5),('헨리',8),('에드워드',9),
           ('에밀리',6),('토마스',4),('헨리',7),('토마스',3),('에밀리',2),('퍼시',5),('고든',13)]

# 제목
print("-------------------------")
print("기차\t총수송량\t순위")
print("-------------------------")

name = []
weight = [] 

trainDic={}
for temp in train_tup:
    name = temp[0]
    weight = temp[1]
    if name in trainDic:
        trainDic[name] += weight
    else:
        trainDic[name] = weight
        
trainlist = sorted(trainDic.items(), key=operator.itemgetter(1), reverse=True)


for x in range(0,len(trainlist)):
    for y in range(0,len(trainlist[0])):
        print(trainlist[x][y], end="\t")
    print("")