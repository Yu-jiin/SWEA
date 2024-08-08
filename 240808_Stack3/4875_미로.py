import sys
sys.setrecursionlimit(10**7)


def findMaze(row, col, N):
    # print(row, col)
    visited[row][col] = 1   # 첫 시작 부분 visited 1로 고쳐주기
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    if maze[row][col] == 3: # 미로의 행과 열이 3(결과)가 되는 순간 return 1
        return 1
    else:
        for x in range(4):  # 델타 시작
            ni = row + di[x]
            nj = col + dj[x]
            if 0 <= ni < N and 0 <= nj < N:     # 범위 내에 있는 확인
                # print(visited)
                if maze[ni][nj] != 1 and visited[ni][nj] == 0:  # 미로에서 1이 아닌 (통로 0이고) 방문한 적이 없다면
                    if findMaze(ni, nj, N):     # 재귀함수로 넣어주기
                        return 1
        return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    # print(maze)

    for i in range(N):  # 출발점 행, 열 구하기 
        for j in range(N):
            if maze[i][j] == 2:
                row = i
                col = j

    visited = [[0] * N for _ in range(N)]   # visited maze와 똑같이 만들어서 0으로 채워주기
    result = findMaze(row, col, N)   # findMaze 함수에 넣어주기

    print(f'#{tc} {result}')
