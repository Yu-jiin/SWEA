import sys
sys.stdin = open('1486.txt', 'r')


def recur(cnt, max_sum):
    global result

    if max_sum >= B:
        result = min(result, max_sum)
        return

    if cnt == N:
        return

    recur(cnt + 1, max_sum + arr[cnt])
    recur(cnt + 1, max_sum)


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    result = 10000000000000

    recur(0, 0)
    print(f'#{tc} {result - B}')