'''
Created on 2019. 4. 16.

@author: user
'''

from CommonDB.Final_DailyBoxoffice import *
from CommonDB.Final_moviedetail import moviedetail
from CommonDB.Final_naver_poster_star import poster

# 일일박스오피스 영화정보 영진위API로 받아와서 txt파일로 저장하고 return
def totalinfo():
    # 변수 정의
    box = dailyrank()
    code = moviecode()
    detail = moviedetail()
    poster_star = poster()
    outfile = None
    outfile2 = None
    
    # text파일 초기화
    outfile = open("movieinfototal.txt", "w")
    outfile.write("")
    outfile.close()
    
    outfile2 = open("movieinfototalstr.txt", "w")
    outfile2.write("")
    outfile2.close()
    
    # 영화 1개당 1줄씩 text파일로 출력
    totalList=[]
    for i in range(0,10):
        totalList.append(box[i] + detail[i] + poster_star[i])
        outfile = open("movieinfototal.txt", "a")
        outlist = "%s" % totalList[i]
        outfile.write(outlist + "\n")
        outfile.close()              
        
        
        codelist=""
        for x in range (len(totalList[i])):
            outfile2 = open("movieinfototalstr.txt", "a")
            codelist += "%s, " % totalList[i][x]
        outfile2.write(codelist + "\n")
        outfile2.close()    
        
    
    print("\t기준일, 순위, 제목, 개봉일, 누적관객수, 코드, 영문이름, 러닝타임, 관람등급, 장르, 감독, 주연, 포스터링크, 별점")
    print("예시) ", totalList[0])
    print()
    print("####### 출력완료 #######")
    
    return totalList

if __name__ == '__main__':
    
    totalinfo()


# totalList = (box)
