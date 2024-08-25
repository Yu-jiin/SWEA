# # 그래프 경로 탐색
#
# def Graph_check(s, V):
#     stack = []
#     visited = [0] * (V+1)
#     result = [s]
#
#     visited[s] = 1
#     v = s
#
#     while True:
#         for a in adjL[v]:
#             if visited[a] == 0:
#                 stack.append(v)
#                 v = a
#                 result.append(v)
#                 visited[a] = 1
#                 break
#         else:
#             if stack:
#                 v = stack.pop()
#             else:
#                 break
#     answer = '-'.join(map(str, result))
#     print(f'#{tc} {answer}')
#
#
# T = 1
# for tc in range(1, T+1):
#     V, E = map(int,input().split())
#     arr = list(map(int, input().split()))
#
#     adjL = [[] for _ in range(V+1)]
#
#     for i in range(E):
#         v1, v2 = arr[i*2], arr[i*2+1]
#         adjL[v1].append(v2)
#         adjL[v2].append(v1)
#     # print(adjL)
#     Graph_check(1, V)

# ----------------------------------------------------------------------
# 경로로 도착 가능하면 1 아니면 0
# def check_graph(start, end, adjL):
#     stack = [start]
#     visited = [0] * (V+1)
#     visited[start] = 1
#
#     while stack:
#         v = stack.pop()
#         if v == end:
#             return 1
#         for a in adjL[v]:
#             if visited[a] == 0:
#                 stack.append(a)
#                 visited[a] = 1
#     return 0
#
#
# T = int(input())
# for tc in range(1, T+1):
#     V, E = map(int, input().split())
#
#     adjL = [[] for _ in range(V+1)]
#     for _ in range(E):
#         A, B = map(int, input().split())
#         adjL[A].append(B)
#
#     start, end = map(int, input().split())
#
#     result = check_graph(start, end, adjL)
#
#     # print(adjL)
#     print(f'#{tc} {result}')

# ---------------------------------------------------
# 미로 찾기
def check_maze(row, col, N):
    global result
    if result == 1:
        return

    visited[row][col] = 1
    di = [0, 1, 0, -1]
    dj = [-1, 0, 1, 0]

    if maze[row][col] == 3:
        result = 1
        return
    else:
        for x in range(4):
            ni = row + di[x]
            nj = col + dj[x]
            if 0 <= ni < N and 0 <= nj < N:
                if maze[ni][nj] != 1 and visited[ni][nj] == 0:
                    check_maze(ni, nj, N)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                row = i
                col = j

    visited = [[0]*N for _ in range(N)]
    result = 0
    check_maze(row, col, N)

    print(f'#{tc} {result}')
