def find_maze(row, col, N):
    global result

    if result == 1:
        return

    visited[row][col] = 1

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    if maze[row][col] == 3:
        result = 1
        return
    else:
        for x in range(4):
            ni = row + di[x]
            nj = col + dj[x]
            if 0 <= ni < N and 0 <= nj < N:
                # 답이 3 이니까 maze[ni][nj] == 0 이 아니라 걍 벽이 아니면
                if maze[ni][nj] != 1 and visited[ni][nj] == 0:
                    find_maze(ni, nj, N)


T = 10
for test_case in range(1, T+1):
    tc = int(input())
    N = 16
    maze = [list(map(int, input().strip())) for _ in range(N)]

    visited = [[0]*N for _ in range(N)]

    # 시작점, 끝점 구하기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                row = i
                col = j
    result = 0

    find_maze(row, col, N)

    print(f'#{tc} {result}')
