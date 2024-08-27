import sys
sys.stdin = open('input.txt')


# def dfs(n):
#     global word
#     if n <= N:
#         # 왼쪽 자식
#         dfs(n * 2)
#         # 알파벳
#         word += arr[n - 1][1]
#         # 오른쪽 자식
#         dfs(n * 2 + 1)
#
#
# T = 10
# for tc in range(1, T+1):
#     N = int(input())
#     tree = [[] for _ in range(N+2)]
#
#     arr = [input().split() for _ in range(N)]
#     word = ''
#     dfs(1)
#     print(arr)
#     print(f'#{tc} {word}')


def inorder(node):
    if node == -1:
        return
    if len(tree[node]) > 0:
        inorder(tree[node][0])
    result.append(node)
    if len(tree[node]) > 1:
        inorder(tree[node][1])


T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr = [input().split() for _ in range(N)]

    tree = [[] for _ in range(N + 1)]

    for i in range(N):
        node_info = arr[i]
        node = int(node_info[0])
        left = str(node_info[1])
        right = int(node_info[2])

        if left != -1:
            tree[node].append(left)
        if right != -1:
            tree[node].append(right)

    result = []
    inorder(1)

    print(f'#{tc} {" ".join(map(str, result))}')
