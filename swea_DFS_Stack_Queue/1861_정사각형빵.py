import sys
sys.stdin = open('1861.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N*N + 1)

    di = [0,1,0,-1]
    dj = [-1,0,1,0]

    for i in range(N):
        for j in range(N):
            for x in range(4):
                ni = i + di[x]
                nj = j + dj[x]
                if nj < 0 or nj >= N or ni < 0 or ni >= N:
                    continue

                if arr[ni][nj] == arr[i][j] + 1:
                    visited[arr[i][j]] = 1
                    break

    cnt, max_cnt, start = 0, 0, 0

    # 뒤에서부터 보는 게 좋다
    for i in range(N*N-1, -1, -1):
        if visited[i]:
            cnt += 1
        else:
            if max_cnt <= cnt:
                max_cnt = cnt
                start = i + 1
            cnt = 1

    print(f'#{tc} {start} {max_cnt}')