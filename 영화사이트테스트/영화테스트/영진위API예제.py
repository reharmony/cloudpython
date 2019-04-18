import json
import math
from urllib.request import urlopen
from urllib.parse import urlencode
from datetime import datetime
from datetime import timedelta

api_key = '54259391886714249219f7f373be933a'

class BoxOffice(object):
    base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/'\
               'searchDailyBoxOfficeList.json'
    def __init__(self, api_key):
        self.api_key = api_key

    def get_movies(self):
        target_dt = datetime.now() - timedelta(days=1)
        target_dt_str = target_dt.strftime('%Y%m%d')
        query_url = '{}?key={}&targetDt={}'.format(self.base_url, self.api_key, target_dt_str)
        with urlopen(query_url) as fin:
            return json.loads(fin.read().decode('utf-8'))

    def simplify(self, result):
        return [
           {
              'rank': entry.get('rank'),
              'rankupdown' : entry.get('rankInten'),
              'name': entry.get('movieNm'),
              'publish': entry.get('openDt'),
              'people': entry.get('audiAcc'),
              'code': entry.get('movieCd')
           }
           for entry in result.get('boxOfficeResult').get('dailyBoxOfficeList')
        ]

box = BoxOffice(api_key)
movies = box.get_movies()
print(box.simplify(movies))
