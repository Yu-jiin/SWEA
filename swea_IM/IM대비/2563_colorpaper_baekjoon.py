paper = [[0] * 100 for _ in range(100)]

black_paper = 10

N = int(input())
for _ in range(N):
    A, B = map(int, input().split())

    for i in range(10):
        for j in range(10):
            paper[A+i][B+j] = 1

count = 0
for a in range(100):
    for b in range(100):
        if paper[a][b] == 1:
            count += 1

print(count)