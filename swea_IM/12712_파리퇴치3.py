# 파리퇴치 3
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    #
    di = [0, 1, 0, -1]
    dj = [-1, 0, 1, 0]