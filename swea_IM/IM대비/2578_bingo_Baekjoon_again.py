def bingo_check(cnt):
    answer = [1] * 5

    # 행 탐색
    for i in range(N):
        if bingo_copy[i] == answer:
            cnt += 1

    # 열 탐색
    for j in range(N):
        col = [bingo_copy[i][j] for i in range(N)]
        if col == answer:
            cnt += 1

    # 대각선 탐색
    c = 0
    for i in range(N):
        if bingo_copy[i][i] == 1:
            c += 1
        if c == 5:
            cnt += 1

    # 역 대각선 탐색
    b = 0
    for i in range(N):
        if bingo_copy[i][N-i-1] == 1:
            b += 1
        if b == 5:
            cnt += 1

    return cnt


bingo = [list(map(int, input().split())) for _ in range(5)]
speak = []
for _ in range(5):
    speak += list(map(int, input().split()))

bingo_copy = [[0]*5 for _ in range(5)]
cnt = 0
N = 5
speak_count = 0

for s in range(25):
    for a in range(N):
        for b in range(N):
            if speak[s] == bingo[a][b]:
                bingo_copy[a][b] = 1
                speak_count += 1
    if speak_count >= 12:
        total_count = bingo_check(cnt)
        if total_count >= 3:
            print(s+1)
            break

