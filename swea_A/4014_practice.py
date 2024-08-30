import sys
sys.stdin = open('4014.txt')

def check(arr, X):
    cnt = 1
    i = 0

    while i < N - 1:
        minus = arr[i + 1] - arr[i]

        # 오르막
        if minus == 1:
            if cnt >= X:
                cnt = 1
            else:
                return 0

        # 내리막
        elif minus == -1:
            if i + X >= N:
                return 0
            for j in range(1, X):
                if arr[i + j] != arr[i + 1]:
                    return 0
            i += X - 1  # 건너뛰기
            cnt = 0

        elif minus == 0:
            cnt += 1

        else:
            return 0

        i += 1

    return 1


# 활주로 건설
T = int(input())
for tc in range(1, T + 1):
    N, X = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    answer = 0
    for row in arr:
        answer += check(row, X)
    for col in zip(*arr):
        answer += check(col, X)

    print(f'#{tc} {answer}')
