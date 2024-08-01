T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    P, A, B = map(int, input().split())

    page = []
    for n in range(1, P+1):
        page.append(n)
    # print(page)

    start = 1
    end = P
    count = 0
    # A
    while start <= end:
        count += 1
        middle = int((start + end) / 2)
        if page[middle] == A:
            break
        elif page[middle] > A:
            end = middle - 1
        else:
            start = middle + 1
    print(count)
    b_count = 0
    # B
    while start <= end:
        b_count += 1
        middle = int((start + end) / 2)
        if page[middle] == B:
            break
        elif page[middle] > B:
            end = middle - 1
        else:
            start = middle + 1
    print(b_count)
    if count < b_count:
        result = 'B'
    elif b_count < count:
        result = 'A'
    else:
        result = 0

    print(f'#{test_case} {result}')
