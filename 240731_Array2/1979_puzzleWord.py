T = int(input())
# 여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    new_arr = [[0] * (N + 2)]
    for row in arr:
        new_arr.append([0] + row + [0])
    new_arr.append([0] * (N + 2))

    count = 0

    for i in range(1, N + 1):
        for j in range(1, N - k + 2):
            if sum(new_arr[i][j:j + k]) == k and new_arr[i][j - 1] == 0 and new_arr[i][j + k] == 0:
                count += 1

    for j in range(1, N + 1):
        for i in range(1, N - k + 2):
            if sum(new_arr[i + l][j] for l in range(k)) == k and new_arr[i - 1][j] == 0 and new_arr[i + k][j] == 0:
                count += 1

    print(f'#{test_case} {count}')

