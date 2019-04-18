'''
Created on 2019. 4. 9.

@author: user
'''
import string

# 영문소문자 목록
a = string.ascii_lowercase
# 10진법 숫자 목록
b = string.digits
# 영문대소문자 목록
c = string.ascii_letters
# 영문 대문자 목록
d = string.ascii_uppercase
# 16진법 숫자 목록
e = string.hexdigits
# 특수문자 목록
f = string.punctuation
# 프린트가능한 문자 모두의 목록
g = string.printable
# 공백문자 목록 (\t,\n 등)
h = string.whitespace

print(b+c+f)

print(a)

print(b)

print(c)

print(d)

print(e)

print(f)

print(g)

print(h)