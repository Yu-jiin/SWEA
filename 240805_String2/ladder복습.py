T = 10
for test in range(1, T + 1):
    tc = int(input())
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 0, -1]
    dj = [-1, 1, 0]

    for j in range(N):
        if arr[99][j] == 2:
            row = 99
            col = j

    while row > 0:
        for x in range(3):
            ni = row + di[x]
            nj = col + dj[x]
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == 1:
                    arr[row][col] = 0
                    row = ni
                    col = nj
                    break

    print(f'#{tc} {col}')
