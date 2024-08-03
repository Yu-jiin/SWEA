T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # target = arr[2][2]

    di = [-2, -1, 1, 2, -2, -1, 1, 2]
    dj = [-2, -1, 1, 2, 2, 1, -1, -2]

    i = 2
    j = 2
    total = arr[2][2]
    for x in range(8):
        ni = i + di[x]
        nj = j + dj[x]
        # print(arr[ni][nj])
        total += arr[ni][nj]

    print(f'#{tc} {total}')
