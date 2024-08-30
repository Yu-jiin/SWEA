import sys
sys.stdin = open('input.txt')


def find_min(x, sum_v):
    global min_sum

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
    N, M = map(int, input().split())
    line = list(map(int, input().split()))

    arr = [list(map(int, input().split())) for _ in range(N)]

    min_sum = float('inf')

    line_min = 0
    col = [0] * N

    for l in line:
        line_min += min(arr[l-1])
        for j in range(N):
            arr[l-1][j] = 0

    find_min(0, 0)
    line_min += min_sum

    print(f'#{tc} {line_min}')
