T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())

    box = [[0] * N for _ in range(N)]

    # arr = list(range(1, (N**2)+1))

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    i = 0   # 행
    j = 0   # 열
    box[i][j] = 1

    count = 1
    num = 1
    while count < N**2:
        for x in range(4):
            ni = i + di[x]
            nj = j + dj[x]
            if 0 <= ni < N and 0 <= nj < N:
                if box[ni][nj] == 0:
                    count += 1
                    box[ni][nj] = count
                    i = ni
                    j = nj
                    break   # for 문 종료시키고 다시 while 문으로 돌아가기

    print(f'#{test_case}')
    for b in box:
        print(*b)

