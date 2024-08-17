def bcount(cnt):
    for i in bingo_copy:
        if i == [1]*5:
            cnt += 1

    for j in range(N):
        col = [bingo_copy[i][j] for i in range(N)]
        if col == [1]*5:
            cnt += 1

    d_count = 0
    for i in range(N):
        if bingo_copy[i][i] == 1:
            d_count += 1
        if d_count == 5:
            cnt += 1

    # if bingo_copy[4][0]==1 and bingo_copy[3][1]==1 and bingo_copy[2][2]==1 and bingo_copy[1][3]==1 and bingo_copy[0][4]==1:
    #     cnt += 1
    b_count = 0
    for i in range(N-1):



    return cnt


N = 5
bingo = [list(map(int, input().split())) for _ in range(N)]
speak = []
for _ in range(5):
    speak += list(map(int, input().split()))

bingo_copy = [[0] * 5 for _ in range(N)]
cnt = 0
# 12부터 계산
speak_count = 0
for s in range(25):
    for i in range(N):
        for j in range(N):
            if speak[s] == bingo[i][j]:
                bingo_copy[i][j] = 1
                speak_count += 1
    if speak_count >= 12:
        bingo_count = bcount(cnt)
        if bingo_count >= 3:
            print(s+1)
            break