import sys
sys.stdin = open('20551.txt', 'r')


def dfs(i):
    global result
    if i == 0:
        return

    if arr[i] > arr[i-1]:
        dfs(i-1)
    else:
        arr[i-1]-1


T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    result = 0

    dfs(len(arr))

