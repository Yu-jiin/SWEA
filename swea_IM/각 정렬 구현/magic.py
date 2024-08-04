N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

K = int(input())

di = [-1, -1, 1, 1]
dj = [-1, 1, -1, 1]

max_count = 0

for i in range(N):
    for j in range(N):
        for a in range(1, K+1):
            target = arr[i][j]  # 꼭 여기에 들어가야하는데 왜 ㅅㅂ
            for x in range(4):
                ni = i + (di[x] * a)
                nj = j + (dj[x] * a)
                if 0 <= ni < N and 0 <= nj < N:
                    target += arr[ni][nj]
                    # print(target)
            if max_count < target:
                # print(max_count)
                max_count = target

print(f'{max_count}')
