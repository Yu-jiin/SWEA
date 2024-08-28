import sys
sys.stdin = open('input.txt')


def dfs(node):

    global answer

    if node == 0:
        return
    if len(tree[node]) > 0:
        dfs(tree[node][0])
    # if node == '/':
    #     answer += tree[node][1] / tree[node][0]
    # elif node == '+':
    #     answer += tree[node][1] + tree[node][0]
    # elif node == '-':
    #     answer += tree[node][1] - tree[node][0]
    # else:
    #     answer += tree[node][1] * tree[node][0]
    calc.append(node)
    if len(tree[node]) > 1:
        dfs(tree[node][1])


T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    # # arr = [list(map(lambda x: int(x) if x.isdecimal() else x, input().split())) for _ in range(N)]
    # arr.insert(0, 0)
    tree = [[] for _ in range(N + 2)]
    for i in range(N):
        while len(arr[i]) < 4:
            arr[i].append(0)
        a, b, c = int(arr[i][0]), int(arr[i][2]), int(arr[i][3])
        if b != 0:
            tree[a].append(b)
        if c != 1:
            tree[a].append(c)

    calc = []
    answer = 0
    dfs(1)

    print(f'#{tc} {calc}')

    # arr = [list(map(lambda x: int(x) if x.isdecimal() else x, input().split())) for _ in range(N)]
    # arr.insert(0, 0)
