'''
1
4 3
1 2 1 2
'''


def dfs(i, sum_v):
    global count

    if sum_v == K:
        count += 1
        return

    if i == N:
        return

    dfs(i + 1, sum_v + arr[i])
    dfs(i + 1, sum_v)


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    count = 0
    dfs(0, 0)

    print(f'#{tc} {count}')