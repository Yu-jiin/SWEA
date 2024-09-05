import sys
sys.stdin = open('input.txt')


def dfs(index, count, sum):
    global result

    if sum < N:
        return

    if index == N:
        result = min(count, result)
        return




T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr.pop(0)
    arr.insert(0, 0)
    result = 101
    dfs(1, 0, 0)

