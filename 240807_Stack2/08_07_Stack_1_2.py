def Graph_search(s, V):
    stack = []
    visited = [0] * (V+1)
    result = [s]    # 첫번째 시작 값 넣고 시작
    # 현재 위치 잡아줘야지 지인아 맞을래
    visited[s] = arr[0]
    v = s   # 현 위치

    while True:
        for p in pair[v]:   # 왜 pair[v]
            if visited[p] == 0:
                stack.append(v)     # 스택에 넣어두고
                v = p               # 출발점 변경해주고
                result.append(v)    # 간 경로 표시해주는 result 에 append 해주고
                visited[p] = 1      # 방문했다고 표시해주기 안가도록
                break
        else:                       #
            if stack:               # 이전 갈림길로 돌아갈 수 있으면
                v = stack.pop()     # 출발지점 돌아가
            else:
                break
    r = '-'.join(map(str, result))
    print(f'#{tc} {r}')



T = 1
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))
    # print(V, E)
    # print(arr)
    pair = [[] for _ in range(V+1)]
    for i in range(E):
        v1, v2 = arr[i*2], arr[i*2+1]
        pair[v1].append(v2)
        pair[v2].append(v1)
    # print(pair)

    Graph_search(1, V)