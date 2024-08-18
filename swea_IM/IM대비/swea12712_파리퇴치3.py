T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [-1, 0, 0, 1]
    dj = [0, -1, 1, 0]

    max_value = 0
    # 가로 세로
    for i in range(N):
        for j in range(N):
            target = arr[i][j]
            row = i
            col = j
            for x in range(4):
                for m in range(1, M):
                    ni = row + di[x] * m
                    nj = col + dj[x] * m
                    if 0 <= ni < N and 0 <= nj < N:
                        target += arr[ni][nj]
            if max_value < target:
                max_value = target

    ci = [1, -1, 1, -1]
    cj = [1, -1, -1, 1]

    # 대각선
    max_value2 = 0
    for a in range(N):
        for b in range(N):
            target2 = arr[a][b]
            r = a
            c = b
            for x in range(4):
                for m in range(1, M):
                    ni2 = r + ci[x] * m
                    nj2 = c + cj[x] * m
                    if 0 <= ni2 < N and 0 <= nj2 < N:
                        target2 += arr[ni2][nj2]
            if max_value2 < target2:
                max_value2 = target2

    if max_value < max_value2:
        max_value = max_value2

    print(f'#{tc} {max_value}')