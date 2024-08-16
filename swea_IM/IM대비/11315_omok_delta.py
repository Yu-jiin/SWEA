T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input().strip())) for _ in range(N)]
    dir = [(1, 0), (0, 1), (1, -1), (1, 1)]
    result = 'NO'

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for x in range(4):
                    row, col = i, j
                    count = 0
                    while 0 <= row < N and 0 <= col < N and arr[row][col] == 'o':
                        count += 1
                        ni, nj = dir[x]
                        row += ni
                        col += nj
                        if count >= 5:
                            result = 'YES'

    print(f'#{tc} {result}')