import sys
sys.stdin = open('4014.txt')


def check(arr, X):
    cnt = 1     # 연속 높이
    global answer
    answer  = 0 # 결과 더하기

    # 평지갈비
    if all(arr[0] == x for x in arr[0:N]):
        answer += 1

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
            if i + X - 1 < N and all(arr[j] == arr[i] for j in range(i, i + X)):
                cnt = 0
            else:
                return 0

        elif minus == 0:
            cnt += 1
        else:
            return 0

    if cnt >= X:
        answer = 1

    return answer


# 활주로 건설
T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 모든 땅이 평지일 때 
    answer = 0
    for row in arr:
        answer += check(row, X)
    for col in zip(*arr):
        answer += check(col, X)

    print(f'#{tc} {answer}')


#  집가서 해보기

