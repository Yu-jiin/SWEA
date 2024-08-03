T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 비교 안해주면 N이 더 길때는 값이 아예 0으로 나옴
    if N < M:
        N, M = M, N
        A, B = B, A

    total_max = 0

    for i in range(N - M + 1):
        max_v = 0
        for j in range(N):
            if 0 <= j < M:
                max_v += A[i+j] * B[j]
        if total_max < max_v:
            total_max = max_v

    print(f'#{tc} {total_max}')
