# 기본
list = [1,5,8,2,3,9,7]
print(min(list))
print(max(list))

# 정렬한 후 최소값 최대값
list.sort()
print(list)
print(min(list))
print(max(list))

# 리스트에서 최소값 찾아서 프린트
list = [2,5,8,1,3,9,7]
print(list.index(min(list)))

# 찾고 싶은 값의 위치 찾기
print(list.index(8))
