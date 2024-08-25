def find_min(x, sum_v):
    global min_sum

    if sum_v >= min_sum:
        return

    if x == N:
        if min_sum > sum_v:
            min_sum = sum_v
            return

    for i in range(N):
        if not col[i]:
            col[i] = 1
            find_min(x+1, sum_v + arr[x][i])
            col[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 100000000
    col = [0] * N

    find_min(0,0)

    print(f'#{tc} {min_sum}')




