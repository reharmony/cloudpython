import requests
import argparse
import sys
from PIL import Image, ImageFilter


API_URL = 'https://kapi.kakao.com/v1/vision/face/detect' # 카카오 비전 얼굴 분석 어플
MYAPP_KEY = '8e358b849511d30bb14a9d0b83129cdc' # REST API 키

# 얼굴사진 정보 함수
def  detect_face(filename):
    headers = {'Authorization':'KakaoAK {}'.format(MYAPP_KEY)}
    # 접속
    try:
        files = {'file':open(filename,'rb')}
        resp = requests.post(API_URL, headers=headers, files=files)
        # 접속 상태 확인
        print(resp)
        resp.raise_for_status()
        print('kakao 비전 서버 접속 OK...')
        return resp.json()
    except Exception as e:
        print(str(e))
        sys.exit(0)
    # 사진 분석 결과를 json으로 받아오기

# 모자이크 처리 함수
def mosiac(filename, detection_result):
    image = Image.open(filename)

    for face in detect_result['result']['faces']:
        x = int(face['x']*image.width)
        w = int(face['w']*image.width)
        y = int(face['y']*image.width)
        h = int(face['h']*image.width)
        box = image.crop((x,y,x+w,y+h))
        box = box.resize((20,20),Image.NEAREST).resize((w,h),Image.NEAREST) # 모자이크 픽셀 가로세로 개수
        image.paste(box, (x,y,x+w,y+h))

    return image



if __name__ == '__main__':
    # 카카오에 접속해서 얼굴사진에 대한 정보 받아오기
    parser = argparse.ArgumentParser(description = 'Mosaic faces...')
    parser.add_argument('image_file', type = str, nargs='?', default = "./img/1.jpg", # 대상 파일
                        help = 'help...') # 쿼리 스트링
    args = parser.parse_args()
    detect_result = detect_face(args.image_file)
    print(detect_result['result']['faces'])
    image = mosiac(args.image_file,detect_result) # image변수에 모자이크 처리된 이미지 담기
    image.show() # 이미지 보기



    # 받아온 정보 중 위치값을 이용해서 모자이크 처리