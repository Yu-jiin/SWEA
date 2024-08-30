import sys
sys.stdin = open('input.txt')

def find_min(x, sum_v):
    global col_count
    global min_sum

    if x == N:
        if min_sum > sum_v:
            min_sum = sum_v
            return

    for i in range (N):
        if not col[i]:
            col[i] = 1
            find_min(x+1, sum_v + arr[x][i])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    col = [0] * N
    col_count = 0

    min_sum = float('inf')

    find_min(0,0)