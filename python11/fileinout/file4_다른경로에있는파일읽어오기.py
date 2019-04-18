'''
Created on 2019. 4. 17.

@author: user
'''
import os

file_name = input("읽어올 파일의 이름을 입력하세요.>> ")
file = "d:/temp/" + file_name + ".txt"

print(os.path.exists(file)) # 현재경로에 해당 파일이 존재하는지 확인

if os.path.exists(file): # 파일이 존재할 시
# fileInput = open("file", "r")
 
    with open(file, "r") as fileInput: # open과 close의 역할을 한번에 수행함
     
        total_line = fileInput.readlines()
        print(total_line)
         
        for x in total_line:
            print(x)
 
else: # 파일이 존재하지 않을 시
    print("해당 파일이 존재하지 않습니다.")  
# fileInput.close()