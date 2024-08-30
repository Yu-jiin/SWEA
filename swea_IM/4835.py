# 구간합
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.


def make_sum(lst):
    sum_value = 0
    for a in lst:
        sum_value += a
    return sum_value


for test_case in range(1, T + 1):
    N, M = (map(int, input().split()))
    # print(N, M)
    arr = list(map(int, input().split()))
    result = []
    for i in range(N-M+1):
        num = arr[i:i+M]
        sum_v = make_sum(num)
        result.append(sum_v)
    print(f'#{test_case} {max(result) - min(result)}')
