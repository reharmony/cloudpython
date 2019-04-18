'''
Created on 2019. 4. 17.

@author: user
'''
import os

print(os.path.exists("data1.txt")) # 현재경로에 해당 파일이 존재하는지 확인

if os.path.exists("data1.txt"): # 파일이 존재할 시
# fileInput = open("data1.txt", "r")

    with open("data1.txt", "r") as fileInput: # open과 close의 역할을 한번에 수행함
    
        total_line = fileInput.readlines()
        print(total_line)
        
        for x in total_line:
            print(x)

else: # 파일이 존재하지 않을 시
    print("해당 파일이 존재하지 않습니다.")  
# fileInput.close()