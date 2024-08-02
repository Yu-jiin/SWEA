
# 델타 탐색을 할때는 무조건 dx,y 를 만들자
dx = [1, 0, 0]
dy = [0, -1, 1]


def search_ladder(x, y):
    # 원본 훼손 X, 방문 체크 할 수 있는 변수
    visited = [[0] * 100 for _ in range(100)]
    # 델타 탐색 순서도 완전 중요함
    visited[x][y] = 1 # 시작지점 방문 체크

    # x 좌표는 행, y 좌표는 열
    # 마지막 행(99)에 도착할 때 까지 델타 탐색 진행
    while x != 99:
        # 3방향 탐색, 근데 언제까지 ?
        for i in range(3):
            nx = x + dx[i]  # 이동한 후의 좌표
            ny = y + dy[i]
            # if 0 <= nx < 100 and 0 <= ny < 100:
            # 이동하려는 좌표가 범위를 벗어난 경우 
            if nx < 0 or nx >= 100 and ny < 0 or ny >= 100:
                continue  
            # 사다리 아닐 때 
            if not data[nx][ny]: continue
            # 이미 방문한 경우
            if visited[nx][ny]: continue

            # 현재 좌표를 방문한 것으로 처리
            visited[x][y] = 1

            # 현재 좌표를 이동하려고 한 좌표로 바꾼다
            x, y = nx, ny
            
    if data[x][y] == 2:
        return True

    return False


for _ in range(1, 11):

    tc = int(input())
    # 100 x 100 2차원 리스트 입력 받는다
    data = [list(map(int, input().split())) for _ in range(100)]

    # 모든 시작점에서 출발해본다
    # 도착지점 2에 제대로 도착했다면, 그 시작점 반환
    # 100 x 100이니가 시작점은 0부터 100까지 모두 다 해야지
    result = -1 # 결과 못 찾을 때
    for j in range(100):
        # 밑에는 길을 찾아가는 로직 작성
        # 사다리는 1, 0은 갈 수 없음
        if data[0][j] == 0:
            continue
        # 여기에 도달한 친구들은 첫 번째 줄에서의 사다리
        # 0,j에서 시작했을 때, 목적지에 도달하는 지 확인
        if search_ladder(0, j):
            # 제대로 도달한 친구는 아래 if 문 코드를 돌린다
            result = j
            break   # if 문 탈출이 아닌 제일 가까운 for/while 탈출

    print(f'#{tc} {result}')
