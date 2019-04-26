'''
Created on 2019. 4. 9.

@author: user
'''
import vlc
import pafy


url = 'https://www.youtube.com/watch?v=ybhXVSAdIRE'
video = pafy.new(url)
best = video.getbest()
media = vlc.MediaPlyer(best.url)
media.play()

