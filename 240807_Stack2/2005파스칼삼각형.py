def pascal(n):
    memo = [[0] * n for _ in range(n)]
    # print(memo)
    for i in range(N):
        for j in range(0, i+1):
            if j == 0 or i == j:
                memo[i][j] = 1
            else:
                memo[i][j] = memo[i-1][j-1] + memo[i-1][j]

    print(f'#{tc}')
    for i in range(N):
        result = ' '.join((map(str, memo[i][:i+1])))
        print(result)
    # print(result)


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    pascal(N)
