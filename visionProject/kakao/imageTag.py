import requests
import argparse
import sys
from collections import Counter
from random import *


API_URL = 'https://kapi.kakao.com/v1/vision/multitag/generate' # 카카오 비전 태그 분석 어플
MYAPP_KEY = '8e358b849511d30bb14a9d0b83129cdc' # REST API 키

# 사진 주소 목록
jeju = [
    'https://search.pstatic.net/common/?src=http%3A%2F%2Fpost.phinf.naver.net%2FMjAxNzAxMDlfODcg%2FMDAxNDgzOTQzNDA5OTU3.A5OW4XegVlVvAZIX-MMPD-rEFhLnB5sp2GrCbNMJZfMg.p9GOCvltQ7T_AQErRaTVYpPx3W5QMPt8-5TGRhhKSMkg.PNG%2FIJMAOFCkriTiVSchbuoVwmcW2_gI.jpg&type=b400',
    'http://post.phinf.naver.net/20150811_4/jtourgolf_14392772921958wlDC_JPEG/mug_obj_201508111614531895.jpg',
    'http://post.phinf.naver.net/20160809_137/14707093077159Oo9g_JPEG/IThxdDBOlQna-K3UnYyp2jZhfErw.jpg',
    'http://blogfiles.naver.net/20150809_47/jjumscand_1439082902218fbWoF_JPEG/%BF%EC%B5%B5.jpg',
    'http://blogfiles.naver.net/20120607_183/jewelrabbit_1339053959590rlFJK_JPEG/%C1%A6%C1%D6%B5%B5_%BF%A9%C7%E022.jpg',
    'http://post.phinf.naver.net/20160420_108/dlrltjs0830_1461118130799TI07O_JPEG/mug_obj_201604201108534670.jpg']

sports = ['http://img.hani.co.kr/imgdb/resize/2019/0121/00503840_20190121.JPG',
          'http://www.wbsc.org/wp-content/uploads/USAvMEX-WBSC-Premier12-2015-TKHR0621-1280x640.jpg',
          'http://image.fnnews.com/resource/media/image/2017/02/10/201702101633328761_l.jpg',
          'http://playkok.co.kr/wp-content/uploads/2017/11/img_yongpyongski10.png',
          'https://sejong.korea.ac.kr/mbshome/mbs/kr/images/sub/hakbu/hakbu_info_2017_030100.jpg',
          'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNeLwsXhiIrWkpX79XFgvjdcyubnSP4EtQzxhHrslQxdd3KRrM']

festival = ['https://pbs.twimg.com/media/CtpGe1NUkAAT00N.jpg',
            'https://t1.daumcdn.net/cfile/tistory/998ED9455BB1FF7636',
            'https://i.ytimg.com/vi/Ge3BtOcBRkQ/hqdefault.jpg',
            'https://t1.daumcdn.net/cfile/tistory/9996DA4C5BB6972710',
            'https://www.gifucvb.or.jp/lang/wp-content/themes/gifucvb2018/image/02/02_02_im_01.jpg',
            'http://morningcalm.co.kr/_ADM/data/goodsImages/part_101529626180.jpg']

# 추천 목록
recommend1 = ['여행','놀이동산','나들이']
recommend2 = ['축구','야구','수영','암벽등반']
recommend3 = ['수목원','식물원','화원']

# 이미지 태그 생성 함수
def generate_tag(image_url):
    headers = {'Authorization':'KakaoAK {}'.format(MYAPP_KEY)}
    # 접속
    try:
        data = {'image_url': image_url}
        resp = requests.post(API_URL, headers=headers, data=data)
        resp.raise_for_status()
        return resp.json()

    except Exception as e:
        print(str(e))
        sys.exit(0)

# 태그 출력 함수
def tag_print(img_url_list):

    alltag = [] # 모든 태그 저장할 리스트
    number = 1  # 사진번호
    for product_url in img_url_list :  # 사진 하나씩 보내서 분석
        parser = argparse.ArgumentParser(description = 'Detect Products.')
        parser.add_argument('image_url', type = str, nargs = '?', default = product_url,
                            help = 'help...')  # 쿼리 스트링
        args = parser.parse_args()
        result_json = generate_tag(args.image_url) # 생성된 태그를 json 형식으로 받아오기
        print("사진%d: " % number, end = "")  # 사진 이름

        for tag in result_json['result']['label_kr'] :  # 사진별 태그 추출
            print("#" + tag, end = " ")
            alltag.append(tag) # 모든 태그를 하나의 리스트에 담기

        number += 1 # 사진번호 증가
        print()

    print()
    print("당신의 태그 목록은", list(set(alltag)), "입니다.")  # 모든 태그 목록을 집합으로 변환해서 중복되는 값을 제거후 다시 리스트로 변경

    count_tag = Counter(alltag)  # Counter함수 사용해서 딕셔너리 형식으로 빈도기준 내림차순 정렬{'태그명':출현횟수}
    most_tag = count_tag.most_common(1)[0][0]  # 가장 빈도 수가 높은 태그명 추출
    print()
    print("당신은 %s(을)를 좋아하시는 군요!!" % most_tag)
    print()

    # 가장 빈도 수가 높은 태그에 따라 추천 목록 지정
    if most_tag == '실외':
        recommend = choice(recommend1)
    elif most_tag == '스포츠':
        recommend = choice(recommend2)
    elif most_tag == '식물':
        recommend = choice(recommend3)

    print(recommend + "을(를) 추천합니다!!")
    print()

if __name__ == '__main__':

    # 사용자 대화 콘솔
    while True:
        select = input('검색할 사진목록을 선택하세요.>> ')
        if select == '1':
            tag_print(jeju)
            print("------------------------------")
        elif select == '2':
            tag_print(sports)
            print("------------------------------")
        elif select == '3':
            tag_print(festival)
            print("------------------------------")
        elif select == '0':
            print("검색을 종료합니다.")
            break

