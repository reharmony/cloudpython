'''
Created on 2019. 4. 12.

@author: user
'''


def codeList():
    
    openfile=None    
    fileList=[]
    codeList=[]
    
    
    openfile = open("moviecode.txt", "r")
    fileList = openfile.read()
    
    a = fileList.split("\n")
    
    for i in range(0,10):
        codeList.append(a[i])
    
    openfile.close()
    
    print(codeList)
    
    return codeList

if __name__ == '__main__':
    codeList()