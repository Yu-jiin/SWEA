import sys
sys.stdin = open('4012.txt')


def dfs(n, k):
    global min_food
    if k == N // 2:
        one, two = 0, 0
        for i in range(N-1):
            for j in range(i+1, N):
                if visited[i] and visited[j]:
                    one += arr[i][j] + arr[j][i]
                elif not visited[i] and not visited[j]:
                    two += arr[i][j] + arr[j][i]
        min_food = min(min_food, abs(one-two))

    for x in range(n, N):
        if not visited[x]:
            visited[x] = 1
            dfs(x+1, k+1)
            visited[x] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    padding = [0] * (N + 1)
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N

    min_food = 100000000000

    dfs(0,0)

    print(f'#{tc} {min_food}')