def Graph_search(s, V):
    stack = []  # DFS에서 사용할 스택을 초기화
    visited = [0] * (V + 1)  # 방문 여부를 기록할 리스트, 0으로 초기화 (V+1 크기)
    result = [s]  # 탐색 경로를 기록할 리스트, 시작 노드를 추가하여 초기화

    # 현재 위치를 현재 노드로 설정
    visited[s] = 1  # 출발 노드를 방문한 것으로 표시
    v = s  # 현재 노드 설정

    while True:
        for p in pair[v]:  # 현재 노드와 연결된 노드들(p)을 순회
            if visited[p] == 0:  # 방문하지 않은 노드인 경우
                stack.append(v)  # 현재 노드를 스택에 추가 (후에 돌아오기 위함)
                v = p  # 현재 노드를 새로운 노드로 변경
                result.append(v)  # 탐색 경로에 새로운 노드 추가
                visited[p] = 1  # 새로운 노드를 방문한 것으로 표시
                break  # 현재 노드에서 새로운 노드를 찾았으므로 반복문을 종료하고 다음 노드로 이동
        else:
            if stack:  # 스택이 비어있지 않으면 (이전에 방문했던 노드가 남아 있으면)
                v = stack.pop()  # 스택에서 노드를 꺼내 현재 노드로 설정 (이전 노드로 돌아가기)
            else:
                break  # 스택이 비어있으면 모든 노드를 탐색한 것이므로 종료

    # 결과 리스트를 문자열로 변환하고 출력 형식에 맞춰 출력
    r = '-'.join(map(str, result))
    print(f'#{tc} {r}')


# 테스트 케이스 수 설정
T = 1
for tc in range(1, T + 1):
    # 정점 수(V)와 엣지 수(E) 입력
    V, E = map(int, input().split())
    # 엣지 정보를 담은 리스트 입력
    arr = list(map(int, input().split()))

    # 인접 리스트를 초기화
    pair = [[] for _ in range(V + 1)]

    # 엣지 정보를 바탕으로 인접 리스트를 구성
    for i in range(E):
        v1, v2 = arr[i * 2], arr[i * 2 + 1]
        pair[v1].append(v2)  # v1에서 v2로 가는 엣지 추가
        pair[v2].append(v1)  # v2에서 v1로 가는 엣지 추가 (무방향 그래프)

    # DFS 탐색 함수 호출, 시작 노드 1에서 탐색 시작
    Graph_search(1, V)
