T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_count = 0

    # 행 탐색
    for row in arr:
        row_count = 0
        current_count = 0
        for i in range(M):
            if row[i] == 1:
                current_count += 1
                row_count = max(row_count, current_count)
            else:
                current_count = 0
        max_count = max(max_count, row_count)

    # 열 탐색
    for j in range(M):
        col_count = 0
        current_count = 0
        for i in range(N):
            if arr[i][j] == 1:
                current_count += 1
                col_count = max(col_count, current_count)
            else:
                current_count = 0
        max_count = max(max_count, col_count)

    print(f'#{tc} {max_count}')
