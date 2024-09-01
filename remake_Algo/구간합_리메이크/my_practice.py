import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    max_row = 0
    for row in arr:
        if max_row < len(row):
            max_row = len(row)

    for row in arr:
        while len(row) < max_row:
            row.append(0)

    max_value = float('-inf')
    min_value = float('inf')
    lst = []
    for j in range(max_row):
        for i in range(N):
            sum_v = 0
            count = 0
            for x in range(i, N):
                if j < len(arr[x]):
                    sum_v += arr[x][j]
                    count += 1
                if count == M:
                    max_value = max(max_value, sum_v)
                    min_value = min(min_value, sum_v)
                    break

    if max_value == float('-inf'):
        max_value = -1

    print(f'#{tc} {max_value - min_value}')
