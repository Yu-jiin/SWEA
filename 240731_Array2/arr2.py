arr1 = [0] * 3

arr2 = [[0] * 3 for _ in range(2)]  # 3행 2열
print(arr1)     # [0, 0, 0]
print(*arr1)    # 언패킹하면 0 0 0

for i in range(2):
    print(*arr2[i])
print('-----------------------------')
s = 0
for i in range(2):  # 행
    for j in range(3):  # 열
        print(arr2[i][j], end=' ')
    print()
print('-----------------------------')
arr = [[1, 2, 3], [4, 5, 6]]
print(len(arr))     # 2개
print(len(arr[0]))  # 3개
print('-----------------------------')
# i = 행  j = 열
# 행의 합 중 최댓값은 ? 행 우선 순회
# 2 1 1
# 1 2 2
# max_v = 0
# for i in range(n):
#     s = 0
#     for j in range(m):
#         f(array[i][j])
#         s += arr[i][j]
#         if max_v < s :
#             max_v = s

# 만약 음수가 가능하다면 ?
# max_value = 0 이 아니겠지 ? ㅠㅠ 문제에 맞는 적절한 작은 값으로


# # 열 우선 순회
# for j in range(m):  # 열
#     for i in range(n):  # 행
#         f(array[i][j])


# 지그재그 순회
# 0 1 2 3
# 3 2 1 0 위아래 더하면 항상 3  3에서 j 값을 빼주면 된다
# j 는 m -1 값
# 증가 = j
# 감소 = m-1-j,   증가 감소 합치면 m-1-2*j
# for i in range(n):
#     for j in range(m):
#         f(array[i][j + (m-1-2*j) * (i%2)])
#  짝수일 때 오른쪽으로 가고 홀수 일때 왼쪽으로 간다
#  짝수이면 (i%2) 이게 0이니까 앞에 식이 날아간다

# for i
#     if i%2 == 0
#         for j : 0
#     else:
#         for 0 : m-1


# 2차원 배열의 접근, 델타 하이라이트 메인 이벤트
# 2차 배열의 한 좌표에서 4방향의 인접배열 요소 탐색
# 오른쪽 a[i]a[j] -> a[i]a[j+1]

