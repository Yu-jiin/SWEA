# 중복 순열

arr = [i for i in range(1, 4)]
visited = [0] * 3


def dfs(level):
    if level == len(arr):
        print(*visited)
        return

    for i in range(len(arr)):
        # 가지치기 : 중복된 숫자 제거
        # if arr[i] in visited:
        #     continue

        visited[level] = arr[i]
        dfs(level + 1)
        # visited[level] = 0


# backtracking(0)
dfs(0)


# 가지를 쳐뿌라 ~~~~~~~~~~
# 1. 깊이우선탐색
# 2. 유망한지 점검    (설계단계에서 유망하지 않은 경우를 생각하고 구현 .. !! )
#   - 반례잡기 참 힘듬 ...............
# 3. 유망하지 않으면 부모노드로 돌아가서 검색
