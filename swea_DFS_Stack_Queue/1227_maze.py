## 재귀로 푸니까 안됨
# def check_maze(row, col):
#     visited[row][col] = 1
#     global result
#     di = [0, 1, 0, -1]
#     dj = [1, 0, -1, 0]
#
#     if maze[row][col] == 3:
#         result = 1
#         return
#
#     for x in range(4):
#         ni = row + di[x]
#         nj = col + dj[x]
#         if 0 <= ni < N and 0 <= nj < N:
#             if maze[ni][nj] != 1 and visited[ni][nj] == 0:
#                 visited[ni][nj] = 1
#                 row = ni
#                 col = nj
#
#
# T = 10
# for test_case in range(1, T+1):
#     tc = int(input())
#     N = 100
#     maze = [list(map(int, input().strip())) for _ in range(N)]
#
#     visited = [[0]*N for _ in range(N)]
#
#     # start
#     for i in range(N):
#         for j in range(N):
#             if maze[i][j] == 2:
#                 row = i
#                 col = j
#
#     result = 0
#     check_maze(row, col)
#
#     print(f'#{tc} {result}')
def find_maze(row, col):
    visited[row][col] = 1

    while


T = 10
for test_case in range(1, T+1):
    tc = int(input())
    N = 100
    maze = [list(map(int, input().strip())) for _ in range(N)]

    visited = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                row = i
                col = j

    find_maze(row, col)
