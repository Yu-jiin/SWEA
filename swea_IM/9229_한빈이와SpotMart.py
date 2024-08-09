T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    total = 0
    sum_v = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if arr[i] + arr[j] <= M:
                sum_v = arr[i] + arr[j]
        if total < sum_v:
            total = sum_v
    if total == 0:
        total = -1

    print(f'#{tc} {total}')
