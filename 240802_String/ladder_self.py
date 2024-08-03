T = 10
for tc in range(1, T+1):
    tc = int(input())
    N = 100
    data = [list(map(int, input().split())) for i in range(N)]
    print(data)

    di = [0, 0, -1]
    dj = [1, -1, 0]

    for j in range(N):
        if data[99][j] == 2:
            row = 99
            col = j

    while row > 0:
        for x in range(3):
            ni = row + di[x]
            nj = col + dj[x]
            if 0 <= ni < N and 0 <= nj < N:
                if data[ni][nj] == 1:
                    data[row][col] = 0  # 지나온 곳은 0으로 표시해서 델타가 가지 못하게
                    row = ni
                    col = nj
                    break

    print(f'#{tc} {col}')
