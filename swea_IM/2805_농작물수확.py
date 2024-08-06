T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    total = 0
    left = N // 2
    right = N // 2

    for i in range(N):
        for j in range(left, right+1):
            total += arr[i][j]
        if i == N//2:
            left += 1
            right -= 1
        else:
            left -= 1
            right += 1
    print(total)

