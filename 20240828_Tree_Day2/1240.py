import sys
sys.stdin = open('input.txt')

decode = {
    '1,0,1,1,0,0,0': 0,
    '1,0,0,1,1,0,0': 1,
    '1,1,0,0,1,0,0': 2,
    '1,0,1,1,1,1,0': 3,
    '1,1,0,0,0,1,0': 4,
    '1,0,0,0,1,1,0': 5,
    '1,1,1,1,0,1,0': 6,
    '1,1,0,1,1,1,0': 7,
    '1,1,1,0,1,1,0': 8,
    '1,1,0,1,0,0,0': 9
}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]

    result = []
    # 0111011 / 0110001 / 0111011 / 0110001 / 0110001 / 0001101 / 0010011 / 0111011
    for row in arr:
        if all(0 == x for x in row[0:N]):
            continue
        row.reverse()
        for i in range(M):
            if row[i] == 1:
                start = i
                break
        break
    for x in range(start, M, 7):
        a = row[x:x+7]
        answer = ','.join(map(str, a))
        if answer in decode:
            result.append(decode[answer])


    result.reverse()

    # 홀, 짝 찾기
    j = 0
    b = 0
    for i in range(len(result)):
        # 홀
        if (i+1) % 2 == 1:
            j += result[i]
        else:
            b += result[i]

    plus = (j*3) + b

    if plus % 10 == 0:
        jiin = sum(result)
    else:
        jiin = 0

    print(f'#{tc} {jiin}')

