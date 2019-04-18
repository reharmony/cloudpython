'''
Created on 2019. 4. 9.

@author: user
'''
import 게시판DB처리

if __name__ == '__main__':
## select문
    print("--------게시판 검색 처리------------------")
    id = input("게시판 ID입력: ")
    result = 게시판DB처리.read(id)
    print(result)
#     a, b, c, d = 게시판DB처리.read(id)
#     print(a, b, c, d)
     
## create문
#     print("--------게시판 삽입 처리------------------")
#     id = input("게시판 ID입력: ")
#     title = input("게시판 제목입력: ")
#     content = input("게시판 내용입력: ")
#     writer = input("게시판 작성자입력: ")
#      
#     게시판DB처리.create(id, title, content, writer)
#      
 
## update문   
#     print("--------게시판 수정 처리------------------")
#     id = input("게시판 ID입력: ")
#     content = input("게시판 내용입력: ")
#     게시판DB처리.update(id,content)
#      
## delete문
#     print("--------게시판 삭제 처리------------------")
#     title = input("게시판 제목입력: ")
#     게시판DB처리.delete(title)

