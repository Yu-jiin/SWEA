
def backtracking(level):
    if level == M:
        print(*visited)
        return

    for i in range(N):
        if arr[i] in visited:
            continue

        visited[level] = arr[i]
        backtracking(level + 1)
        visited[level] = 0


N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
visited = [0] * M

backtracking(0)
