T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = [[0] * N for i in range(N)]
    # print(arr)

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    i = 0
    j = 0
    arr[i][j] = 1
    count = 1
    while count < N**2:
        for x in range(4):
            while True:
                ni = i + di[x]
                nj = j + dj[x]
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
                    # if arr[ni][nj] == 0:
                    count += 1
                    arr[ni][nj] = count
                    i = ni
                    j = nj
                else:
                    break
    print(f'{tc}')
    for a in arr:
        print(*a)