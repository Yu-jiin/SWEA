# 선택 정렬
# 주어진 자료들 중 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식
# 정렬기준 - 오름차순
# 1. 리스트 중 최솟값을 찾는다
# 2. 그 값을 리스트의 맨 앞에 위치한 값과 교환
# 3. 맨 처음 위치를 제외한 나머지 리스트를 대상으로 과정 반복

# min_idx = 0
# if a[min_idx] > a[i]:
#     min_idx = i     그러면 리스트의 맨 앞에 위치한 값과 교환
# 인덱스 값만 알고 있으면 값을 알 수 있음
# min_idx = 1
# if a[min_idx] > a[i]:
#     min_idx = i     그러면 리스트의 맨 앞에 위치한 값과 교환
# 기준 위치는 N - 2 or N - 1

# for i : 0 -> N-2 기준 위치
# min_idx = i   현재 구간의 맨앞을 최소로 가정
# for j : i + 1 -> N-1 비교구간 원소
# if a(min_idx) > a[i]:
#     min_idx = i

def selection_sort(arr, N):  # 정렬 대상, N 크기
    # 주어진 구간에 대해 .. 기준위치 i를 정하고
    for i in range(N-1):    # N-2 까지니까 N-1로
        min_idx = i  # 최솟값 위치를 기준 위치로 가정
        for j in range(i+1, N):
            if arr[min_idx] > arr[j]:
                min_idx = j
        # 구간의 최솟값을 기준 위치로 이동
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


A = [2, 7, 5, 3, 4]
B = [4, 3, 2, 1]
selection_sort(A, len(A))
selection_sort(B, len(B))
print(A)
print(B)



