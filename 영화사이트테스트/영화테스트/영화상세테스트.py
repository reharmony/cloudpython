import requests

response = requests.get('http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?'\
'key=54259391886714249219f7f373be933a&movieCd=20196244')

data1 = response.json()['movieInfoResult']
data2 = data1['movieInfo']
print(data2)