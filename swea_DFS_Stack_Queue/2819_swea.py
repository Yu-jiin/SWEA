import sys
sys.stdin = open('2819.txt', 'r')
# set 사용


def dfs(i, j, num):
    if len(num) == 7:
        result.add(num)
        return

    for x in range(4):
        ni = i + di[x]
        nj = j + dj[x]
        if nj < 0 or nj >= 4 or ni < 0 or ni >= 4:
            continue

        dfs(ni, nj, num + arr[ni][nj])


T = int(input())
for tc in range(1, T+1):
    arr = [input().split() for _ in range(4)]
    di = [0,1,0,-1]
    dj = [-1,0,1,0]
    result = set()

    for i in range(4):
        for j in range(4):
            dfs(i, j, arr[i][j])

    print(f'#{tc} {len(result)}')
