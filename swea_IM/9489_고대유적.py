T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) + [2] for _ in range(N)]     # list out of range 방지용 2추가
    # print(arr)

    # 행 탐색
    count = 0
    first_count = 1
    for row in arr:
        for i in range(M):
            if row[i] == 1 and row[i+1] == 1:   # 처음꺼랑 다음꺼가 1 이라면 카운트
                first_count += 1
                if count < first_count:
                    count = first_count
            else:
                first_count = 0     # 초기화

    count2 = 0
    second_count = 1
    for i in range(N):
        for j in range(M):
            col = [arr[i][j] for i in range(N)]
            col.append(2)
            # print(col)
            for x in range(len(col)-1):
                if col[x] == 1 and col[x+1] == 1:
                    second_count += 1
                    if count2 < second_count:
                        count2 = second_count
                else:
                    second_count = 0

    max_v = 1
    if count < count2:
        max_v = count2
    else:
        max_v = count

    print(f'#{tc} {max_v+1}')
