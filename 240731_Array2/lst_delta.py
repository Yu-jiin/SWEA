T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
#  5 x 5
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, -1, 1, 0]
    dj = [1, 0, 0, -1]

    total = 0
    for i in range(N):
        for j in range(N):
            sum_value = 0
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    sum_value += abs(arr[i][j] - arr[ni][nj])    # 절대값 처리 해주기
            total += sum_value
    print(f'#{test_case} {total}')

    lst = arr[i][j: j + k]