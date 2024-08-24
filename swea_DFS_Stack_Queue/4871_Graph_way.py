def DFS(S, G, arr):
    visited = [0] * (V + 1)
    stack = [S]
    visited[S] = 1

    while stack:
        v = stack.pop()
        if v == G:
            return 1
        for w in arr[v]:
            if visited[w] == 0:
                stack.append(w)
                visited[w] = 1

    return 0


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())

    # 인접리스트 input 받는 대로 바로 집아넣기
    arr = [[] for _ in range(V + 1)]
    for _ in range(E):
        A, B = map(int, input().split())
        arr[A].append(B)
        # print(arr)
    S, G = map(int, input().split())

    result = DFS(S, G, arr)

    print(f'#{tc} {result}')