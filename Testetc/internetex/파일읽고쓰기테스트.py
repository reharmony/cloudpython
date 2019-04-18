'''
Created on 2019. 4. 12.

@author: user
'''

openfile=None
outfile = None
fileList=[]


openfile = open("moviecode.txt", "r")
fileList = openfile.read()
List=[]
a = fileList.split("\n")

for i in range(0,10):
    List.append(a[i])
print(List)

openfile.close()

