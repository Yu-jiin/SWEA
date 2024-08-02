T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    P, A, B = map(int, input().split())
    # page = []
    # for n in range(1, P+1):
    #     page.append(n)
    start = 0
    end = P

    count = 0
    # A
    while start <= end:
        count += 1
        middle = int((start + end) / 2)
        if middle == A:
            break
        elif middle > A:
            end = middle
        else:
            start = middle
    # print(count)

    b_count = 0
    # B
    while start <= end:
        b_count += 1
        middle = int((start + end) / 2)
        print(middle)
        if middle == B:
            break
        elif middle > B:
            end = middle
        else:
            start = middle

    if count < b_count:
        result = 'A'
    elif b_count < count:
        result = 'B'
    else:
        result = 0

    print(f'#{test_case} {result}')
