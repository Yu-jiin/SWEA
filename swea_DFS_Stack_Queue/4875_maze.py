def check_maze(row, col, N):
    global result
    if result == 1:
        return

    visited[row][col] = 1
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    if arr[row][col] == 3:
        result = 1
        return
    else:
        for x in range(4):
            ni = row + di[x]
            nj = col + dj[x]
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] != 1 and visited[ni][nj] == 0:
                    check_maze(ni, nj, N)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    # 출발점 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                row = i
                col = j

    # 방문한거 찍어주기
    visited = [[0]*N for _ in range(N)]

    result = 0
    check_maze(row, col, N)

    print(f'#{tc} {result}')