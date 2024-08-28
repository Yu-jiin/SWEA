import sys
sys.stdin = open('input.txt')

def dfs(node):
    if node == 0:
        return 0

    if len(tree[node]) == 0:
        return int(arr[node - 1][1])

    if len(tree[node]) > 0:
        left = dfs(tree[node][0])
    else:
        0

    if len(tree[node]) > 1:
        right = dfs(tree[node][1])
    else:
        0

    x = arr[node - 1][1]

    if x == '+':
        return left + right
    elif x == '-':
        return left - right
    elif x == '*':
        return left * right
    elif x == '/':
        return left / right


T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    tree = [[] for _ in range(N + 2)]

    for i in range(N):
        while len(arr[i]) < 4:
            arr[i].append(0)
        a, b, c = int(arr[i][0]), int(arr[i][2]), int(arr[i][3])
        if b != 0:
            tree[a].append(b)
        if c != 0:
            tree[a].append(c)

    answer = dfs(1)

    # 결과 출력
    print(f'#{tc} {int(answer)}')
