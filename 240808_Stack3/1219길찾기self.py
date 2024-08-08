def DFS(adjL):
    stack = []
    visited = [0] * 100
    v2 = 0
    visited[v2] = 1
    stack.append(v2)

    while True:
        for w in adjL[v2]:
            if visited[w] == 0:
                stack.append(v2)
                v2 = w
                visited[w] = 1
                break
        else:
            if stack:
                v2 = stack.pop()
            else:
                break
    return visited[99]



T = 10
for test_case in range(1, T+1):
    tc, E = map(int, input().split())
    arr = list(map(int, input().split()))
    adjL = [[] for _ in range(100)]

    for i in range(E):
        v1, v2 = arr[i * 2], arr[i * 2 + 1]
        adjL[v1].append(v2)
    # print(adjL)

    print(f'#{tc} {DFS(adjL)}')
