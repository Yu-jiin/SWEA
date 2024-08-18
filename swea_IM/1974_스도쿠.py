T = int(input())
for tc in range(1, T+1):
    N = 9
    arr = [list(map(int, input().split())) for _ in range(N)]

    number = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    row = 0
    col = 0
    other = 0

    # # 행
    # for i in range(N):
    #     if arr[i].sort() == number:
    if all(sorted(arr[i]) == number for i in range(N)):
        row = 1

    # 열
    if all(sorted([arr[i][j] for i in range(N)]) == number for j in range(N)):
        col = 1

    count = 0
    # 3 * 3 배열
    for a in range(0, N, 3):
        for b in range(0, N, 3):
            test = []
            for x in range(3):
                for y in range(3):
                    test.append(arr[a+x][b+y])
            if sorted(test) == number:
                count += 1
            if count == 9:
                other = 1

    if row == 1 and col == 1 and other == 1:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
