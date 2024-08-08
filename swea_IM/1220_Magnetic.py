T = 10
for tc in range(1, T+1):
    N = int(input(100))
    table = [list(map(int, input().split())) for _ in range(N)]

    for j in range(N):
