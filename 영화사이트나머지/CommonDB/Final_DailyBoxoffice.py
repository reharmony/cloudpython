import requests
import copy
import datetime
from datetime import timedelta



def dailyrank():
    
    today = datetime.date.today() - timedelta(1)
    yesterday = today.strftime('%Y%m%d')
    
    # 영화진흥위 API 요청
    response = requests.get('http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/'\
                   'searchDailyBoxOfficeList.json?key=54259391886714249219f7f373be933a&targetDt=%s' % yesterday)
    
    # json 형식으로 변수에 저장
    data = response.json()
    
    # 다중 딕셔너리&리스트 형태임. 'boxOfficeResult'키에 속한 값 가져오기 
    data2 = data['boxOfficeResult']
    
    # 그중에서 'dailyBoxOfficeList'에 속한 값 가져오기
    data3 = data2['dailyBoxOfficeList']
    
    # 변수 선언
    data4={}
    data6=[]
    
    # 필요한 키 값만 추출하기 (순위, 영화명, 개봉일, 누적관객수, 영화코드) 
    for i in range(0,10):        
        data4['selectDay'] = (data2['showRange'][0:8])
        data4['rank'] = data3[i]['rank']
        data4['name'] = data3[i]['movieNm']
        data4['openDay'] = data3[i]['openDt']
        data4['totalPeople'] = data3[i]['audiAcc']
        data4['code'] = data3[i]['movieCd']
        data5 = copy.deepcopy(data4)
        data6.append(data5)
    
    
    # 최종결과 확인   
#     print(data6)
    outfile = ""
    outfile = open("movieinfo.txt", "w")
    infostr="" 
    infolist=[]
    box=[]
    for i in range(0,10):
#       infostr = "%s,%s,%s,%s,%s" % (data6[i]['rank'],data6[i]['name'],data6[i]['openDay'].replace('-','.'),data6[i]['totalPeople'],data6[i]['code'])
        infolist=[]
        infolist.append(data6[i]['selectDay'])
        infolist.append(data6[i]['rank'])
        infolist.append(data6[i]['name'])
        infolist.append(data6[i]['openDay'].replace('-','.'))
        infolist.append(data6[i]['totalPeople'])
        infolist.append(data6[i]['code'])        
        infostr = "%s" % infolist + "\n" 
        outfile.write(infostr)
        box.append(infolist)
        print(infolist)        
    outfile.close()
    
    
    # 영화이름 출력
    outfile = ""
    outfile = open("moviename.txt", "w")
    namelist=""
    for i in range(0,10):
        namelist = "%s" % data6[i]['name']
        outfile.write(namelist + "\n")
    outfile.close()
    
    return box

        
def moviecode():
   
    today = datetime.date.today() - timedelta(1)
    yesterday = today.strftime('%Y%m%d')
    
    # 영화진흥위 API 요청
    response = requests.get('http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/'\
                   'searchDailyBoxOfficeList.json?key=54259391886714249219f7f373be933a&targetDt=%s' % yesterday)
    
    # json 형식으로 변수에 저장
    data = response.json()
#     print(data['showRange'])
    # 다중 딕셔너리&리스트 형태임. 'boxOfficeResult'키에 속한 값 가져오기 
    data2 = data['boxOfficeResult']
    # 그중에서 'dailyBoxOfficeList'에 속한 값 가져오기
    data3 = data2['dailyBoxOfficeList']
#     print(data3)
    # 변수 선언
    data4={}
    data6=[]
    
    # 필요한 키 값만 추출하기 (순위, 영화명, 개봉일, 누적관객수, 영화코드) 
    for i in range(0,10):     
        data4['code'] = data3[i]['movieCd']
        data5 = copy.deepcopy(data4)
        data6.append(data5)
    
    
    # 영화코드   출력    
    outfile = ""
    outfile = open("moviecode.txt", "w")
    codelist=""
    for i in range(0,10):
        codelist = "%s" % data6[i]['code']
        outfile.write(codelist + "\n")
    outfile.close()           
        
if __name__ == '__main__':
    
    rank = dailyrank()
    code = moviecode()
   

