import json
import math
from urllib.request import urlopen
from urllib.parse import urlencode
from datetime import datetime
from datetime import timedelta

api_key = '54259391886714249219f7f373be933a'

class BoxOffice(object):
    base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/'\
               'searchMovieInfo.json'
    def __init__(self, api_key):
        self.api_key = api_key

    def get_movies(self):
#         target_dt = datetime.now() - timedelta(days=1)
#         target_dt_str = target_dt.strftime('%Y%m%d')
        query_url = '{}?key={}&movieCd={}'.format(self.base_url, self.api_key, '20196244')
        with urlopen(query_url) as fin:
            return json.loads(fin.read().decode('utf-8'))

    def simplify(self, result):
        return [
           {
              'name': entry.get('movieNm'),
              'type': entry.get('typeNm'),
              'dir': entry.get('directors'),
              'dir_name': entry.get('peopleNm'),
              'show':entry.get('showTypeNm'),
              'audult':entry.get('auditNo')
           }
            for entry in result.get('movieResult').get('MovieInfo')
        ]
    
box = BoxOffice(api_key)
movies = box.get_movies()
print(box.simplify(movies))

# print(movies)