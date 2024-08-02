T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())

    box = [[0] * N for _ in range(N)]

    arr = list(range(1, (N**2)+1))

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    box[0][0] = 1
    x = 0   # 행
    y = 0   # 열
    count = 1

    while count < N**2:
        num = 1
        for x in range(4):
            ni = x + di[x]
            nj = y + dj[x]
            if 0 <= ni < N and 0 <= nj < N:
                if box[ni][nj] == 0:
                    box[ni][nj] = num + 1
                    count += 1
                    x = ni
                    y = nj
                    break

    print(box)