'''
Created on 2019. 4. 9.

@author: user
'''

### 전역변수 활용 (global)

count = 0

def javaCount():
    global count # global을 사용해서 전역변수 count임을 선언
    count = count + 1
    print(count)

def pythonCount():
    global count
    count = count + 1
    print(count)

    


if __name__ == '__main__':
    javaCount()
    pythonCount()
    javaCount()
    pythonCount()
    javaCount()
    pythonCount()
    javaCount()
    pythonCount()
    javaCount()
    pythonCount()
 