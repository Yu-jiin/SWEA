T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input().strip())) for _ in range(N)]

    result = ''
    # 가로체크
    num = 5
    for i in range(N):
        for j in range(N - 5 + 1):
            if arr[i][j:j+5] == ['o'] * 5:
                result = 'YES'
                break

    # 세로 체크
    if result == 'NO':
        for i in range(N):
            for j in range(N-4):
                if [arr[x][i] for x in range(j, j+5)] == ['o'] * 5:
                    result = 'YES'
                    break

    # all 함수
    # 반복문 내에 조건이 모두 참인지 확인해주는 함수

    # 대각선 체크
    if result == 'NO':
        for i in range(N-4):
            for j in range(N-4):
                if all(arr[i+k][j+k] == 'o' for k in range(5)):
                    result = 'YES'
                    break

    # 역대각선 체크
    if result == 'NO':
        for i in range(4, N):
            for j in range(N-4):
                if all(arr[i-k][j+k] == 'o' for k in range(5)):
                    result = 'YES'
                    break

    print(f'#{tc} {result}')

    # T = int(input())
    # for tc in range(1, T + 1):
    #     N = int(input())
    #     arr = list(input() for _ in range(N))
    #     dir = [(1, 0), (0, 1), (1, -1), (1, 1)]
    #     result = 'NO'
    #     for i in range(N):
    #         for j in range(N):
    #             if arr[i][j] == 'o':
    #                 for k in range(4):
    #                     row, col = i, j
    #                     cnt = 0
    #                     while 0 <= row < N and 0 <= col < N and arr[row][col] == 'o':
    #                         cnt += 1
    #                         dir_r, dir_c = dir[k]
    #                         row += dir_r
    #                         col += dir_c
    #                         if cnt >= 5:
    #                             result = 'YES'
    #     print(f'#{tc} {result}')
