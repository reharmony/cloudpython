import requests
import copy
import datetime
from datetime import timedelta
from CommonDB.Code_Read import codeList

def moviedetail():
    
    outfile = None
    outfile = open("moviedetail.txt", "w")
    codelist=""
    outfile.write(codelist)
    outfile.close()
    
    detail=[]
    
    for i in range(0,10):
    
        # 변수 선언    
        data4=[]
        data6=[]
        data7=[]
        data8=[]
        
        today = datetime.date.today() - timedelta(1)
        yesterday = today.strftime('%Y%m%d')
        code = codeList()[i]
         
        # 영화진흥위 API 요청    
        response = requests.get('http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?'\
                                'key=54259391886714249219f7f373be933a&movieCd=%s' % code)
         
        # json 형식으로 변수에 저장
        data = response.json()
         
         
        # 다중 딕셔너리&리스트 형태임. 'movieInfoResult'키에 속한 값 가져오기 
        data2 = data['movieInfoResult']
         
         
        # 그중에서 'dailyBoxOfficeList'에 속한 값 가져오기
        data3 = data2['movieInfo']
      
        # 필요한 키 값만 추출하기 (순위, 영화명, 개봉일, 누적관객수)
        data4.append(data3['movieCd'])
        data4.append(data3['movieNmEn'])
        data4.append(data3['showTm'])
         
        data_genres = data3['genres']
        data_directors = data3['directors']
        data_actors = data3['actors']
        data_age = data3['audits']
        
        data4.append(data_age[0]['watchGradeNm'])
        
        # 장르 추출
        if len(data_genres) < 2:
            data4.append(data_genres[0]['genreNm'])
        else:
            for i in (0,len(data_genres)-1):
                data6.append(data_genres[i]['genreNm'])    
            data4.append(data6)
        
        # 감독 추출
        if len(data_directors) < 2:
            data4.append(data_directors[0]['peopleNm']) 
        else:
            for i in (0,len(data_directors)-1):
                data7.append(data_directors[i]['peopleNm'])    
            data4.append(data7)
          
        # 배우 추출
        if len(data_actors) < 2:
            data4.append(data_actors[0]['peopleNm'])
        else:
            for i in (0,len(data_actors)-1):
                data8.append(data_actors[i]['peopleNm'])    
            data4.append(data8)
      
        print()

        detail.append(data4[1:7])
        
        data4.append(data3['openDt'])
 
        outfile = None
        outfile = open("moviedetail.txt", "a")
        codelist=""
        codelist = "%s" % data4
        outfile.write(codelist + "\n")
        outfile.close()
       
        
        print("상세 데이터")
        print("영화코드, 영문제목, 러닝타임, 관람등급, 개봉일, 장르, 감독, 주연")
        print(data4)
      
    return detail
     
if __name__ == '__main__':
    moviedetail()


