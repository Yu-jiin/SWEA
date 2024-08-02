T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())    # 당근개수
    C = list(map(int, input().split()))  # 당근의 크기

    C.append(0)
    # print(C)

    # 중복제거
    count = 0   # 제일 큰 카운트
    now = 1     # 현재

    for i in range(1, N):
        if C[i] > C[i-1]:
            now += 1
        else:
            if count < now:
                count = now
            now = 1
        if now > count:
            count = now

    print(f'#{test_case} {count}')