import sys
sys.stdin = open('4014.txt')

def check(lst, v):
    cnt = 1

    for i in range(1, len(lst)):
        if lst[i-1] == lst[i]:
            cnt += 1
        elif lst[i - 1] + 1 == lst[i] and cnt >= X and v[i - X:i] == [0] * X:
            cnt = 1
            v[i - X:i] = [1] * X
        elif lst[i - 1] > lst[i]:
            cnt = 1
        else:  # 2이상
            return False
    return True


# 활주로 건설
T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    answer = 0

    for _ in range(2):
        for lst in arr:
            visited = [0] * (len(lst))
            # 역방향, 방향 모두 ㄱㅊ으면
            if check(lst, visited) and check(lst[::-1], visited[::-1]):
                answer += 1
        arr = list(map(list, zip(*arr)))

    print(f'#{tc} {answer}')

