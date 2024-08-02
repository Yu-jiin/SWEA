T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for test_case in range(1, T + 1):
    n = len(A)
    N, K = map(int, input().split())
