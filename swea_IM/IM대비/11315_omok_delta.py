T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]
    di = [1, 0, 1, 1]
    dj = [0, 1, -1, 1]

    result = 'NO'

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for x in range(4):
                    row, col = i, j
                    count = 0
                    if 0 <= row < N and 0 <= col < N and arr[row][col] == 'o':
                        count += 1
                        ni = row + di[x]
                        nj = col + dj[x]
                        row += ni
                        col += nj
                        if count >= 5:
                            result = 'YES'

    print(f'#{tc} {result}')