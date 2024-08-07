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
    print(count)
    # print(arr)

    # print('--------------------')
    min_value = 1000000

    for a in range(1, N-1):
        for b in range(a+1, N):
            count1 = 0
            for i in range(1, a):   # 흰 파 빨 나누는 기준점을 a, b 로 잡기
                count1 += sum(1 for j in range(M) if arr[i][j] != 'W')
            for i in range(a, b):
                count1 += sum(1 for j in range(M) if arr[i][j] != 'B')
            for i in range(b, N - 1):
                count1 += sum(1 for j in range(M) if arr[i][j] != 'R')

            if min_value > count1:
                min_value = count1
    
    total = min_value + count

    print(f'#{tc} {total}')