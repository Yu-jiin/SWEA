# 파리퇴치 3
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 가로세로 델타
    di = [0, 1, 0, -1]
    dj = [-1, 0, 1, 0]

    # 대각선 델타
    ci = [1, -1, -1, 1]
    cj = [1, -1, 1, -1]


