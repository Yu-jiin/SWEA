T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    L, R = [list(map(int, input().split())) for _ in range(Q)]
    print(L)
    box = [0] * N
    for l in L:
        for r in R:
            for i in range(1, l+1):
                box[i] = l


    # for i in range(1, L+1):
    #     box[i] = L

    print(box)