import sys
sys.stdin = open('2819.txt', 'r')


def dfs(i, j, word):
    global result

    if len(word) == 7:
        result.add(word)
        return

    for x in range(4):
        ni = i + di[x]
        nj = j + dj[x]
        if nj < 0 or nj >= 4 or ni < 0 or ni >= 4:
            continue
        dfs(ni, nj, word+arr[ni][nj])


T = int(input())
for tc in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)]
    count = 0
    result = set()

    di = [0, 1, 0, -1]
    dj = [-1, 0, 1, 0]

    for i in range(4):
        for j in range(4):
            dfs(i, j, arr[i][j])

    for a in range(len(result)):
        count += 1

    print(f'#{tc} {count}')