T = int(input())
for tc in range(1, T+1):
    arr = [list([0] * 10) for _ in range(10)]
    N = int(input())
    count = 0

    for _ in range(N):
        i1, i2, j1, j2, color = map(int, input().split())
        for i in range(i1, j1 + 1):
            for j in range(i2, j2 + 1):
                if arr[i][j] == 0:
                    arr[i][j] = color
                elif arr[i][j] != color:
                    arr[i][j] = 3
                    count += 1
    print(f'#{tc} {count}')
