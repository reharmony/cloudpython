'''
Created on 2019. 4. 17.

@author: user
'''
fileInput = open("data1.txt", "r")
while True:
    line = fileInput.readline()
    if line == "":
        break
    print(line)
fileInput.close()