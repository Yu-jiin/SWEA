T = 10
for test_case in range(1, T + 1):
    tc = int(input())
    N = 100
    arr = [list(map(str, input().split())) for _ in range(N)]

    # print(arr)

    # # 가로부터 비교
    # new_lst = []
    # for i in arr:
    #     for j in range(1, N):
    #         arr[i: i+j]

