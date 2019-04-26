'''
Created on 2019. 4. 12.

@author: user
'''


outfile = None
outfile = open("moviecode.txt", "w")
codelist=""
for i in range(0,10):
    codelist = "%s" % data6[i]['code']
    outfile.write(codelist + "\n")
outfile.close()