import sys
sys.stdin = open('input.txt')


def dfs(n):
    global word
    if n <= N:
        # 왼쪽 자식
        dfs(n * 2)
        # 알파벳
        word += arr[n - 1][1]
        # 오른쪽 자식
        dfs(n * 2 + 1)


T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [[] for _ in range(N+2)]

    arr = [input().split() for _ in range(N)]
    word = ''
    dfs(1)
    print(arr)
    print(f'#{tc} {word}')
