T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_len = 1
    carrot = [arr[0]]

    for i in range(1, N):
        if arr[i] > arr[i-1]:
            carrot.append(arr[i])
        else:
            carrot = [arr[i]]

        if max_len < len(carrot):
            max_len = len(carrot)


    print(f'#{tc} {max_len}')