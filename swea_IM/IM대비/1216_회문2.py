# 가장 긴 회문
#  N = 100 일때 가장 긴 회문
#  100으로 시작해서 회문 찾고 나오는 순간 문제 끝
# 슬라이싱 연습
N = 10
M = 10
arr = [[1,2,3,4,5,6,7,8,9,10] for _ in range(N)]

# for i in range(N):
#     row = arr[i]
#     length = len(row)
#     for start in range(length):
#         for end in range(start +1, length +1):
#             sliced = row[start:end]
#             print(f'Row {i}, {sliced}')

# # 행 5개씩 슬라이싱
# slice_l = 5
# for i in range(N):
#     row = arr[i]
#     l = len(row)
#     for start in range(l - slice_l + 1):
#         end = start + slice_l
#         slice_part = row[start:end]
#         print(f'Row {i}, Slice {start}:{end} -> {slice_part}')


# #  열 5개씩 슬라이싱
# slice_l = 5
# for j in range(M):
#     for i in range(N):
#         col = [arr[i][j] for i in range(N)]
#
#     for start in range(len(col) - slice_l + 1):
#         end = start + slice_l
#         sliced_part = col[start:end]
#         print(f'Column {j}, Slice {start}:{end} -> {sliced_part}')


# 모든 열 슬라이싱
for j in range(M):
    col = [arr[i][j] for i in range(N)]
    for start in range(N):
        for end in range(start+1, N+1):
            sliced_part = col[start:end]
            print(sliced_part)

# T = 10
# for test_case in range(1, T + 1):
#     tc = int(input())
#     N = 100
#     arr = [input().strip() for _ in range(N)]
#
#     max_value = 1
#     max_word = ""
#     # 행 비교
#     for i in range(N):
#         for j in range(N):
#             for k in range(j, N):
#                 string1 = ""
#                 for l in range(j, k+1):
#                     string1 += arr[i][l]
#                 # print(string1)






