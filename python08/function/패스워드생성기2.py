'''
Created on 2019. 4. 8.

@author: user
'''
### 패스워드 생성기2 ###

import random

# 함수 정의
def makePass(passList):
    rand=""  
    idxNum=0
    for x in range(0,3):
        for y in range(0,5):
            idxNum = random.randrange(len(passList))
            rand += passList[idxNum]
        print(rand)
        rand = ""

# 메인
if __name__ == '__main__':
    passList = ['a','b','c','d','e','1','2','3','4','5']
      
    makePass(passList)
    