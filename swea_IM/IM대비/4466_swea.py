T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort(reverse=True)

    score = 0
    for i in range(M):
        score += arr[i]

    print(f'#{tc} {score}')
