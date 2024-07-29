# 1
# 5
# 477162 658880 751280 927930 297191
# 결과값 : #1 630739
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_v = arr[0]
    for i in range(1, N):
        if max_v < arr[i]:
            max_v = arr[i]

    min_v = arr[0]
    for i in range(1, N):
        if min_v > arr[i]:
            min_v = arr[i]
    print(f'#{tc} {max_v - min_v}')