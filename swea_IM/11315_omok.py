T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 5 ~20
    arr = [list(map(str, input().strip())) + ['/']*5 for _ in range(N)]
    # print(arr)
    result = 'NO'

    num = 5
    omok = ['o'] * 5
    # 행 탐색
    for row in arr:
        for i in range(N):
            # print(row[i:i+num])
            if row[i:i+num] == omok:
                result = 'YES'
                break

    # 열 탐색
    if result == 'NO':
        for j in range(N):
            for i in range(N):
                col = [arr[i][j] for i in range(N)]
            for start in range(len(arr) - num + 1):
                end = start + num
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
                        for k in range(1, num):
                            ni = i + di[d] * k
                            nj = j + dj[d] * k
                            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
                                count += 1
                            else:
                                break
                        if count == num:
                            result = 'YES'
                            break
                if result == 'YES':
                    break
            if result == 'YES':
                break


    print(f'#{tc} {result}')