T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(N)]
    new_arr = [[0] * (N + 2)]
    for row in arr:
        new_arr.append(row)
    new_arr.append([0] * (N+2))
    # print(new_arr)

    answer = [0] + ([1] * K) + [0]
    answer_len = len(answer)

    # 행 탐색
    count = 0
    for row1 in new_arr:
        for start in range(N+2 - answer_len + 1):
            end = start + answer_len
            if row1[start:end] == answer:
                count += 1

    # 열 탐색
    count2 = 0
    for j in range(N+2):
        col = [new_arr[i][j] for i in range(N + 2)]
        for s in range(N+2 - answer_len + 1):
            e = s + answer_len
            slice_part = col[s:e]
            if slice_part == answer:
                count2 += 1

    result = count + count2

    print(f'#{tc} {result}')

