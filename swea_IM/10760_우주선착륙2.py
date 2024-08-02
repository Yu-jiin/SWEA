T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for i in range(N)]

    di = [-1, -1, -1, 0, 0, 1, 1, 1]
    dj = [-1, 0, 1, -1, 1, -1, 0, 1]

    result = 0
    for i in range(N):
        for j in range(M):
            target = arr[i][j]
            count = 0
            for x in range(8):
                ni = i + di[x]
                nj = j + dj[x]
                if 0 <= ni < N and 0 <= nj < M:
                    if arr[ni][nj] < arr[i][j]:
                        count += 1
            if count >= 4:
                result += 1
    print(f'#{test_case} {result}')
