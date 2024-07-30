T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    room = int(input())
    boxs = list(map(int, input().split()))
    boxlist = [0] * room
    max = 0
    for idx in range(room):
        count = 0
        for c in range(idx + 1, room):
            if boxs[idx] > boxs[c]:
                count += 1
            if count > max:
                max = count
    print(f'#{test_case} {max}')

