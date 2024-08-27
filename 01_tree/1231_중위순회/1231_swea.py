import sys
sys.stdin = open('input.txt')


def inorder(node):
    if node == -1:
        return
    if len(tree[node]) > 0:
        inorder(tree[node][0])
    result.append(arr[node-1][1])
    if len(tree[node]) > 1:
        inorder(tree[node][1])


T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr = [input().split() for _ in range(N)]

    tree = [[] for _ in range(N + 2)]
    for i in range(N):
        while len(arr[i]) < 4:
            arr[i].append(-1)
        a, b, c = int(arr[i][0]), int(arr[i][2]), int(arr[i][3])
        if b != -1:
            tree[a].append(b)
        if c != -1:
            tree[a].append(c)

    result = []
    inorder(1)

    print(f'#{tc} {"".join(map(str, result))}')
