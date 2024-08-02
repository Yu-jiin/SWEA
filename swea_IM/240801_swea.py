T = 1
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())
    result = []
    for n in range(1, N + 1):
        n = str(n)
        count = 0
        for a in n:
            if a in '369':
                count += 1
        if count > 0:
            result.append('-'*count)
        else:
            result.append(n)

    print(' '.join(result))
