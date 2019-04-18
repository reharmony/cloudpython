'''
Created on 2019. 4. 9.

@author: user
'''
### 파일의 경로 찾기 ###
import os
### 달력 ###
import calendar

if __name__ == '__main__':
    # 달력 출력
    cal = calendar.month(2019,4)
    print(cal)
    
    # 현재 파일 경로 출력
    print(os.getcwd())
    # 하위 폴더와 파일 출력
    print(os.listdir("."))
    
    # 경로 지정
    os.chdir("c:")
    # 지정된 경로 출력
    print(os.getcwd())
    # 하위 폴더와 파일 출력
    print(os.listdir("."))