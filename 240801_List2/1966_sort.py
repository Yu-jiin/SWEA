T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    num = list(map(int, input().split()))

    # min_value = num[0]

    for i in range(N - 1):
        min_idx = i
        for j in range(i + 1, N):
            if num[min_idx] > num[j]:
                min_idx = j
        num[i], num[min_idx] = num[min_idx], num[i]

    print(f'#{test_case} {" ".join(map(str, num))}')

