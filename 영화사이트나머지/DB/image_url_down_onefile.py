'''
Created on 2019. 4. 21.

@author: jeong
'''
import shutil
import requests
from PIL import Image

def poster_down_resize(poster_url):
    # 포스터 다운로드
    poster_name = poster_url[49:66]
    response = requests.get(poster_url, stream=True)
    print(response)
    with open('%s.jpg' % poster_name, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    
    # 포스터 리사이즈
    basewidth = 200
    img = Image.open('%s.jpg' % poster_name)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    img.save('%s.jpg' % poster_name) 
    
    return poster_name