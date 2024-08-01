# 정렬 안되있으면 ?
# for i in range(n):
#     if a[i] == key:
#         return i
# return -1
#
# def s(a, n, key):
#     i = 0
#     while i < n and a[i]!=key:  # 배열 끝이거나, 키를 찾으면 중단
#         i = i + 1
#     if i < n:
#         return i  # 값을 찾아서 중단 
#     else:
#         return -1

# 자료가 오름차순으로 정렬된 상태에서 검색
# 배열에서 12를 찾는데 12가 없고 정렬된 상태에서 14가 나온다면 그냥 중단
# for i in n
#     if a[i] == key
#         return i
#     elif a[i] > key:
#         return -1
# return -1
#
# def s(a,n,key)
#     i = 0
#     while i < n and a[i]<key: # 항상 인덱스 검사가 먼저 .. !! 단축평가
#         i += 1
#     if i<n and a[i] == key:
#         return i
#     else:
#         return -1

