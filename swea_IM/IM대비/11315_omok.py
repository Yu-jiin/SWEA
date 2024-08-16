T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input().strip())) for _ in range(N)]

    omok = ['o'] * 5
    result = 'NO'

    # 행 탐색
    for row in arr:
        for i in range(N):
            # print(row[i:i+num])
            if row[i:i+5] == omok:
                result = 'YES'
                break

    # 열 탐색
    if result == 'NO':
        for j in range(N):
            for i in range(N):
                col = [arr[i][j] for i in range(N)]
            for start in range(N - 5 + 1):
                end = start + 5
                slice_part = col[start:end]
                if slice_part == omok:
                    result = 'YES'
                    break

    # 대각선 탐색
    if result == 'NO':
        di = [1, 1, -1, -1]
        dj = [1, -1, 1, -1]
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 'o':
                    for d in range(4):
                        count = 1
                        for k in range(1, 5):
                            ni = i + di[d] * k
                            nj = j + dj[d] * k
                            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
                                count += 1
                            else:
                                break
                        if count == 5:
                            result = 'YES'
                            break
                if result == 'YES':
                    break
            if result == 'YES':
                break


    # # 오른 대각
    # if result == 'NO':
    #     result_list = []
    #     for i in range(N - 5 + 1):
    #         for j in range(N - 5 + 1):
    #             for k in range(5):
    #                 if arr[i+k][j+k] == 'o':
    #                     result_list.append('o')
    #                     if result_list == omok:
    #                         result = 'YES'
    #                         break
    #                 else:
    #                     result_list = []
    #
    # # 왼 대각
    # if result == 'NO':
    #     result_list2 = []
    #     for a in range(4, N):
    #         for b in range(N - 5 + 1):
    #             for k in range(5):
    #                 if arr[a-k][b+k] == 'o':
    #                     result_list2.append('o')
    #                     if result_list2 == omok:
    #                         result = 'YES'
    #                         break
    #                 else:
    #                     result_list2 = []

    print(f'#{tc} {result}')
