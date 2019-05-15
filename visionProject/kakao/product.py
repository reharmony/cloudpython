import requests
import argparse
import sys
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO


API_URL = 'https://kapi.kakao.com/v1/vision/product/detect' # 카카오 비전 상품 분석 어플
MYAPP_KEY = '8e358b849511d30bb14a9d0b83129cdc' # REST API 키

# 상품 정보 분석 함수
def detect_product(image_url):
    headers = {'Authorization':'KakaoAK {}'.format(MYAPP_KEY)}
    # 접속
    try:
        data = {'image_url': image_url}
        resp = requests.post(API_URL, headers=headers, data=data)
        # 접속 상태 확인
        print(resp)
        resp.raise_for_status()
        print('kakao 비전 서버 접속 OK...')
        return resp.json()

    except Exception as e:
        print(str(e))
        sys.exit(0)
    # 사진 분석 결과를 json으로 받아오기

# 이미지에 상품 표시 하는 함수
def show_products(image_url, detection_result):
    try:
        image_resp = requests.get(image_url)
        image_resp.raise_for_status()
        file_jpgdata = BytesIO(image_resp.content)
        image = Image.open(file_jpgdata)
    except Exception as e:
        print(str(e))
        sys.exit(0)

    # 네모 그리기
    draw = ImageDraw.Draw(image)
    for obj in detection_result['result']['objects']:
        x1 = int(obj['x1']*image.width)
        y1 = int(obj['y1']*image.height)
        x2 = int(obj['x2']*image.width)
        y2 = int(obj['y2']*image.height)
        draw.rectangle([(x1,y1), (x2, y2)], fill=None, outline=(255,0,0,255))
        draw.text((x1+5,y1+5), obj['class'], (255,0,0))
    del draw

    return image



if __name__ == '__main__':
    # 카카오에 접속해서 사진에 대한 정보 받아오기
    product_url = 'http://www.fashionn.com/files/board/2017/image/p1bqqkbadljj81024a411g04m981.jpg' # 대상 이미지 주소
    parser = argparse.ArgumentParser(description = 'Detect Products.')
    parser.add_argument('image_url', type = str, nargs='?', default = product_url,
                        help = 'help...') # 쿼리 스트링
    args = parser.parse_args()

    detection_result = detect_product(args.image_url)
    image = show_products(args.image_url, detection_result)
    image.show() # 이미지 보기


