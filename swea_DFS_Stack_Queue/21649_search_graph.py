T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))

    adjL = [[] for _ in range(V+1)]
    for i in range(E):
