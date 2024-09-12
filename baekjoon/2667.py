def dfs(x, y):
    global cnt

    arr[x][y] = 0
    cnt += 1

    for i in range(4):
        ni = x + di[x]
        nj = y + dj[x]
        if ni < 0 or ni >= N or nj < 0 or nj >= N:
            continue
        if arr[ni][nj] == 1:
            dfs(ni, nj)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]
result = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            cnt = 0
            dfs(i, j)
            result.append(cnt)


print(cnt)