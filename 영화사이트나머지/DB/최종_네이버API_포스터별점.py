import os
import sys
import urllib.request
import json



def poster():
    for i in range(0,10):            
        openfile=None    
        fileList=[]
        nameList=[]
        
        
        openfile = open("movieinfo.txt", "r")
        fileList = openfile.read()
        
        a = fileList.split("\n")
        nameList = a[i]       
        openfile.close()    
        print(nameList)    
        
        client_id = "y2ojBn2tSStkUq1zVx51"
        client_secret = "nKd9wpjDJZ"
        encText = urllib.parse.quote("캡틴마블")
        url = ("https://openapi.naver.com/v1/search/movie.json?query=%s&display=1&start=1" % encText) # json 결과
        # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # json 결과
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            decode = json.loads(response_body.decode('utf-8'))
            items = decode.get('items')    
            poster = items[0]['image'] + "," + items[0]['userRating']
            outfile = None
            outfile = open("poster_star.txt", "a")
            codelist="" 
            codelist = poster
            outfile.write(codelist + "\n")
            outfile.close()
           
        else:
            print("Error Code:" + rescode)
            
        
if __name__ == '__main__':
    poster()