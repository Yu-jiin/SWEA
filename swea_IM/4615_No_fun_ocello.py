# 종나 재미없는 오셀로 게임
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0] * (N+1) for _ in range(N+1)]
    arr[N//2][N//2] = arr[N//2+1][N//2+1] = 2
    arr[N // 2][N // 2+1] = arr[N // 2 + 1][N // 2] = 1
    # print(arr)
    di = [-1, -1, -1, 0, 0, 1, 1, 1]
    dj = [-1, 0, 1, -1, 1, -1, 0, 1]

    for _ in range(M):
        i, j, color = map(int, input().split())
        arr[i][j] = color
        for x in range(8):
            change = []
            for m in range(1, N):
                ni = i + di[x]*m
                nj = j + dj[x]*m
                if 1 <= ni <= N and 1 <= nj <= N:
                    if arr[ni][nj] == 0:
                        break
                    elif arr[ni][nj] == color:
                        while change:
                            ti, tj = change.pop()
                            arr[ti][tj] = color
                        break
                    else:
                        change.append((ni, nj))
                else:
                    break

    black = 0
    white = 0
    for lst in arr:
        black += lst.count(1)
        white += lst.count(2)
    print(f'#{tc} {black} {white}')

# 빠빠이




