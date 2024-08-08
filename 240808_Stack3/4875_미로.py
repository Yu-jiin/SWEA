import sys
sys.setrecursionlimit(10**7)


def findMaze(row, col, N):
    print(row, col)
    visited[row][col] = 1
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    if maze[row][col] == 3:
        return 1
    else:
        for x in range(4):
            ni = row + di[x]
            nj = col + dj[x]
            if 0 <= ni < N and 0 <= nj < N:
                # print(visited)
                if maze[ni][nj] != 1 and visited[ni][nj] == 0:
                    if findMaze(ni, nj, N):
                        return 1
        return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    # print(maze)

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                row = i
                col = j

    visited = [[0] * N for _ in range(N)]
    findMaze(row, col, N)
    print(f'#{tc} {findMaze(row, col, N)}')
