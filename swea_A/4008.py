

def dfs(level, total):
    global min_value
    global max_value

    if level == N:
        min_value = min(min_value, total)
        max_value = max(max_value, total)
        return

    for i in range(4):
        if plus[i] == 0:
            continue

        plus[i] -= 1
        dfs(level +1, calcu)
        plus[i] += 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    plus = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    min_value = -1000000000
    max_value = 1000000000

    dfs(0, 0)