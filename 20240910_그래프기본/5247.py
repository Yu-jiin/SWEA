from collections import deque

def bfs():
    que = deque([(N, 0)])
    visited = [0]*(10**6+1)
    while que:
        now, count = que.popleft()
        # 해당 숫자를 이미 방문한 경우
        if visited[now]:
            continue
        # 방문하지 않는 숫자인 경우
        visited[now] = 1
        if now == M:
            return count
        count += 1
        if 0 < now - 1 <= 10**6:
            que.append((now-1, count))
        if 0 < now + 1 <= 10**6:
            que.append((now+1, count))
        if 0 < now * 2 <= 10**6:
            que.append((now*2, count))
        if 0 < now - 10 <= 10**6:
            que.append((now-10, count))


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    result = bfs()
    print(f'#{tc} {result}')

'''
3
2 7
3 15
36 1007
'''