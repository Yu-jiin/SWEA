# N = 5
# arr = [[0] * N for _ in range(N)]
#
# for r in range(N):
#     for c in range(0, r + 1):
#         arr[r][c] = 1
#
# for lst in arr:
#     print(*lst)

memo = [[0] * 10 for _ in range(10)]

for n in range(10):
    for r in range(0, n + 1):
        if r == 0 or n == r:
            memo[n][r] = 1
        else:
            memo[n][r] = memo[n-1][r-1] + memo[n-1][r]

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    print(f'#{tc}')
    for n in range(N):
        for r in range(0, n + 1):
            print(memo[n][r], end=' ')
        print()

for i in range(10):
    print(*memo[i][:i+1])
