import copy
T = 10
for test_case in range(1, T+1):
    tc = int(input())
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [1, 0, 0]
    dj = [0, -1, -1]

    min_count = 1000000
    result_col = 0

    for j in range(N):
        if arr[0][j] == 1:
            row = 0
            col = j
        visited = [[False]*N for _ in range(N)]    # 원본 리스트 손상 방지
        count = 0
        while row != 99:
            visited[row][col] = True
            for x in range(3):
                ni = row + di[x]
                nj = col + dj[x]
                if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                    if arr[ni][nj] == 1:
                        count += 1
                        row = ni
                        col = nj
                        break
        if min_count >= count:
            min_count = count
            result_col = j


    print(f'#{tc} {result_col}')

    # col_list = []
    # for j in range(N):
    #     if arr[0][j] == 1:
    #         row = 0
    #         col = j
    #         col_list.append(col)
    # # print(col_list)
