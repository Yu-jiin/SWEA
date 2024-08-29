import sys
sys.stdin = open('4014.txt')


def check(arr, X):
    cnt = 1
    global answer

    # 경사로 설치갈비
    for i in range(1, N):
        minus = arr[i] - arr[i - 1]
        # 오르막
        if minus == 1:
            if cnt >= X:
                cnt = 1
            else:
                return 0

        # 내리막
        elif minus == -1:
            cnt = 1
            for j in range(i + 1, i + X):
                if j >= N or arr[i] != arr[j]:
                    return 0
            i += (X - 1)

        # 평지갈비
        elif minus == 0:
            cnt += 1
        else:
            return 0

    return 1


# 활주로 건설
T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    answer = 0
    for row in arr:
        answer += check(row, X)
    for col in zip(*arr):
        answer += check(col, X)

    print(f'#{tc} {answer}')


#  집가서 해보기

