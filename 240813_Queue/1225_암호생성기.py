T = 10
for test_case in range(1, T+1):
    tc = int(input())

    arr = list(map(int, input().split()))

    while arr[-1] != 0:
        for x in range(1, 6):
            if arr[0] - x > 0:
                arr.append(arr[0]-x)
                arr.pop(0)
            else:
                arr.append(0)
                arr.pop(0)
                break

    result = ' '.join(map(str, arr))

    print(f'#{tc} {result}')

