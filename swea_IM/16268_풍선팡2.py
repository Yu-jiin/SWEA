T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    max_total = 0
    for i in range(N):
        for j in range(M):
            target = arr[i][j]
            total = target
            for x in range(4):
                ni = i + di[x]
                nj = j + dj[x]
                if 0 <= ni < N and 0 <= nj < M:
                    total += arr[ni][nj]
            if max_total < total:
                max_total = total

    print(f'#{test_case} {max_total}')