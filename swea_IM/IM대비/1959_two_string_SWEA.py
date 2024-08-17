T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    max_v = 0

    # 이거안하면 N이 더 길때 값 아예 0으로 나옴
    if N < M:
        N, M = M, N
        A, B = B, A

    for i in range(N-M+1):
        sum_v = 0
        for j in range(N):
            if 0 <= j < M:
                sum_v += A[i+j] * B[j]

        if max_v < sum_v:
            max_v = sum_v

    print(f'#{tc} {max_v}')


