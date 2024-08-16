T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 정답 패턴 생성
    answer = [1] * K

    # 행과 열 탐색
    result = 0

    # 행 탐색
    for row in arr:
        count = 0
        for i in range(N):
            if row[i] == 1:
                count += 1
            else:
                if count == K:
                    result += 1
                count = 0
        if count == K:
            result += 1

    # 열 탐색
    for col in range(N):
        count = 0
        for row in range(N):
            if arr[row][col] == 1:
                count += 1
            else:
                if count == K:
                    result += 1
                count = 0
        if count == K:
            result += 1

    print(f'#{tc} {result}')
