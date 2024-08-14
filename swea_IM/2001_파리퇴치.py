T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # di = [0, 1, 1]
    # dj = [1, 0, 1]

    total_count = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            count = 0
            for a in range(M):
                for b in range(M):
                    count += arr[i+a][j+b]

            if total_count < count:
                total_count = count

    print(f'#{tc} {total_count}')