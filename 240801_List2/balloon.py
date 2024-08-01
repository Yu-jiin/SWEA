T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for n in range(N)]
    max_sum = 0
    for i in range(N):
        for j in range(M):
            target = arr[i][j]
            total = target
            for y in range(1, target+1):
                di = [0, y, 0, -y]
                dj = [y, 0, -y, 0]
                for x in range(4):
                    ni = i + di[x]
                    nj = j + dj[x]
                    if 0 <= ni < N and 0 <= nj < M:
                        total += arr[ni][nj]
            if max_sum < total:
                max_sum = total

    print(f'#{test_case} {max_sum}')


    # di = [0, 1, 0,-1]
    # dj = [1, 0, -1, 0]
    # maxValue = 0
    #
    # for i in range(N):
    #     for j in range(M):
    #         target = arr[i][j]
    #         # s = 0
    #         for k in range(4):
    #             total = 0
    #             for plus in range(target):
    #                 ni = i + di[k] + plus
    #                 nj = j + dj[k] + plus
    #                 if 0 <= ni < N and 0 <= nj < N:
    #                     total += (arr[i][j] + arr[ni][nj])
    #                     if maxValue < total:
    #                         maxValue = total
    # print(maxValue)
    #

