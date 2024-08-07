def DFS(g1, g2, v1):
     visited = [0] * 100
     stack = []
     visited[v1] = 1
     stack.append(v1)

     while stack:
         for w in [g1[v1], g2[v2]]:
             if w != -1 and not visited[w]:
                 visited[w] = 1
                 stack.append(v1)
                 v1 = w
                 break



T = 10
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))

    g1 = [-1] * 100
    g2 = [-1] * 100

    for i in range(E):
        v1, v2 = arr[i*2], arr[i*2+1]
        if g1[v1] == -1:
            g1[v1] = v2
        else:
            g2[v1] = v2

    ans = DFS(g1, g2, 0)
