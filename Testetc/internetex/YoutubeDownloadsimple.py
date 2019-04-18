from pytube import YouTube
 
yt = YouTube('https://www.youtube.com/watch?v=846cjX0ZTrk') #다운로드 받고자 하는 url을 입력합니다.
 
print(yt.title)
yt.streams.first().download()