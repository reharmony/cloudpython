import requests
import copy
import datetime
from datetime import timedelta

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

# 필요한 키 값만 추출하기 (순위, 영화명, 개봉일, 누적관객수) 
for i in range(0,10):
    data4['rank'] = data3[i]['rank']
    data4['name'] = data3[i]['movieNm']
    data4['openDay'] = data3[i]['openDt']
    data4['tatalPeople'] = data3[i]['audiAcc']
    data5 = copy.deepcopy(data4)
    data6.append(data5)

# 최종결과 확인   
print(data6)
