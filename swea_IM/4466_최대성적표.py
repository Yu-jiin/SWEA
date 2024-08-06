T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    score = list(map(int, input().split()))
    # print(N, M)
    score.sort(reverse=True)
    # print(score)

    total = 0
    for i in range(M):
        total += score[i]

    print(f'#{test_case} {total}')
