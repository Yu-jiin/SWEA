T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    number = list(map(int, input().strip()))

    max_v = max(number)

    counts = [0] * (max_v + 1)

    for n in number:
        counts[n] += 1

    max_count = 0
    max_num = 0
    for i in range(len(counts)):
        if counts[i] > max_count or (counts[i] == max_count and i > max_num):
            max_count = counts[i]
            max_num = i

    print(f'#{test_case} {max_num} {max_count}')
