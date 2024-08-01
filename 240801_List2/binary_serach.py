# 이진 검색
# 목적 키를 찾을 때 까지 이진 검색을 순환적으로 반복 수행하면서
# 검색 범위를 반으로 줄여가며 보다 빠르게 검색 수행
#
# 이진 검색은 반드시 자료가 정렬된 상태

# 중간 원소 찍고 key 보다 중간원소가 크면 그 범위는 검색 제외
# 1. 검색 범위의 시작점, 종료점 이용하여 검색 반복 수행
# 2. 이진 검색의 경우 자료의 삽입이나 삭제가 발생했을 때 배열의 상태를 항상 정렬하는 추가작업 필요
#
# 짝수일 때
# (start + end) // 2
# start + (end - start) // 2 등 일정한 규칙 필요
# 0 + 4 // 2
#
# 홀수일 때 (0 + 3) // 2 -> 1
# 그럼 그냥 1부터
# while  start <= end 남은 구간이 있으면(원소가 하나라도 있으면 해야함)
#   mid = (start + end) // 2
#   if a[mid] == key
#         return mid
#   if a[mid] < key:
#       start = mid +1
#   else:
#       end = mid -1

# while
#     if a[mid] == key
#     elif a[mid] > key
#         emd = mid -1
#     else

# 이진탐색트리 - 삽입삭제정렬이 매우 빠른 자료 구조


