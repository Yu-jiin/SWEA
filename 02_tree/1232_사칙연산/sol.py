import sys
sys.stdin = open('input.txt')

def dfs(node):
    global answer

    if node == 0:
        return
    if len(tree[node]) > 0:
        dfs(tree[node][0])
    calc.append(arr[node-1][1])
    if len(tree[node]) > 1:
        dfs(tree[node][1])

T = 10
for tc in range(1, T+1):
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

    calc = []
    dfs(1)

    answer = 0
    i = 0
    while i < len(calc):
        if calc[i].isdigit():
            answer = int(calc[i])
        else:
            x = calc[i]
            if i+1 < len(calc) and calc[i+1].isdigit():
                next = int(calc[i+1])
                if x == '+':
                    answer += next
                elif x == '-':
                    answer -= next
                elif x == '*':
                    answer *= next
                elif x == '/':
                    answer /= next
                i += 1
        i += 1

    print(f'#{tc} {int(answer)}')