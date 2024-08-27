import sys
sys.stdin = open('input.txt')

def dfs(node):
    global count

    if node == -1:
        return count

    order.append(node)
    count += 1
    dfs(tree[node][0])
    dfs(tree[node][1])



T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    tree = [[] for _ in range(E+2)]

    for i in range(E):
        a, b = arr[i * 2], arr[i * 2 + 1]
        tree[a].append(b)

    for i in range(E+2):
        while len(tree[i]) < 2:
            tree[i].append(-1)

    count = 0
    order = []

    dfs(N)

    print(f'#{tc} {count}')