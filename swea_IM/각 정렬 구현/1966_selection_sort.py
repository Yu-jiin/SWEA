T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    # for i in range(N):
    #     min_idx = i
    #     for j in range(i+1, N):
    #         if arr[j] < arr[min_idx]:
    #             min_idx = j
    #         arr[i], arr[min_idx] = arr[min_idx], arr[i]
    # #       제발 arr[i], arr[min_idx]다..
    # result = ' '.join(map(str, arr))
    # print(f'#{tc} {result}')

    for i in range(N):
        min_idx = i
        for j in range(i+1, N):
            if arr[j] < arr[min_idx]:
                min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    result = ' '.join(map(str, arr))
    print(f'#{tc} {result}')
