T = 10
for test_case in range(1, T + 1):
    tc = int(input())
    N = 100
    arr = [list(map(str, input().split())) for _ in range(N)]

    # print(arr)

    for i in range(N):
        for j in range(N):
            print(arr[:i])

