# 농작물 수확하기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]

    left = N // 2
    right = N // 2
    middle = N // 2
    count = 0

    for i in range(N):
        for j in range(left, right + 1):
            count += arr[i][j]
        if i < middle:
            left -= 1
            right += 1
        else:
            left += 1
            right -= 1

    print(f'#{tc} {count}')