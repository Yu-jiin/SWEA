T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().strip()))
    arr.append(0)
    # print(arr)
    total_count = 0
    count = 0
    for i in range(N):
        if arr[i] == 1:
            arr[i] == arr[i+1]
            count += 1
        else:   # 만약에 arr[i]으로 시작하는데 totalcount 보다 작으면 초기화
            count < total_count
            count = 0
        if total_count < count:
            total_count = count

    print(f'#{tc} {total_count}')
