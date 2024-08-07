T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    # print(arr)
    count = 0
    for i in range(N):
        for j in range(M):
            if arr[0][j] != 'W':
                count += 1
                arr[0][j] = 'W'
            if arr[N-1][j] != 'R':
                count += 1
                arr[N-1][j] = 'R'
            # if
    total = count
    # print(count)
    # print(arr)
    max_color = 0   # 행마다 제일 많은 색깔 개수 

    print('--------------------')
    # 흰
    white_count = 0
    blue_count = 0
    red_count = 0
    for i in range(1+i, N-1-i):
        # for j in range(M):
        print(arr[i])
        if arr[1+i][N-1-i] != 'W':
            white_count += 1
            arr[1+i][N-1-i] = 'W'
        for j in range(N-1-i, N-1-i-j):
            pass

# w = arr[i].count('W')
# b = arr[i].count('B')
# r = arr[i].count('A')
# print(f'w = {w}, b = {b}, r = {r}')

    

    print(f'#{tc} {count}')