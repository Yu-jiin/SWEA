# 파리퇴치 3
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 가로세로 델타
    di = [0, 1, 0, -1]
    dj = [-1, 0, 1, 0]

    # 대각선 델타
    ci = [1, -1, -1, 1]
    cj = [1, -1, 1, -1]

    max_value = 0
    total = 0
    max_value2 = 0
    for i in range(N):
        for j in range(N):
            target = arr[i][j]
            for x in range(4):
                for m in range(1, M):
                    ni = i + di[x] * m
                    nj = j + dj[x] * m
                    if 0 <= ni < N and 0 <= nj < N:
                        target += arr[ni][nj]
            if max_value < target:
                max_value = target

    for i in range(N):
        for j in range(N):
            target = arr[i][j]
            for x in range(4):
                for m in range(1, M):
                    ni = i + ci[x] * m
                    nj = j + cj[x] * m
                    if 0 <= ni < N and 0 <= nj < N:
                        target += arr[ni][nj]
            if max_value2 < target:
                max_value2 = target

    if max_value > max_value2:
        total = max_value
    else:
        total = max_value2

    print(f'#{tc} {total}')
