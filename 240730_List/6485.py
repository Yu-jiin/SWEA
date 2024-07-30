# 삼성시의 버스 노선
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, T + 1):
    N = int(input())
    counts = [0] * 5001

    for _ in range(N):
        b1, b2 = (map(int, input().split()))
        # print(b1, b2)
        for i in range(b1, b2+1):
            counts[i] += 1

    p = int(input())
    answer = []
    for _ in range(p):
        c = int(input())
        answer.append((counts[c]))

    print(f'#{test_case}', ' '.join(map(str, answer)))



