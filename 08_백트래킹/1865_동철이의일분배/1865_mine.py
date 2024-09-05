import sys
sys.stdin = open('input.txt')


def dfs(index, percent):
    global max_sum

    # 개쌉필요 ... 터져터져
    if max_sum >= percent:
        return

    if index == N:
        max_sum = max(percent, max_sum)
        return

    for x in range(N):
        if not visited[x]:
            visited[x] = 1
            dfs(index+1, percent * arr[index][x])
            visited[x] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr =[list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    for i in range(N):
        for j in range(N):
            arr[i][j] = arr[i][j] * 0.01

    max_sum = -100000000000

    dfs(0, 1)
    result = max_sum * 100
    r = format(result, '.6f')

    print(f'#{tc} {r}')
