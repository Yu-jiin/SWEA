N, M = map(int, input().split())
line_count = int(input())
# paper = [[1] * N for _ in range(M)]
# print(paper)
row = [0, M]    # 행 값 넣어
col = [0, N]    # 열 값 넣어

for _ in range(line_count): #       0-가로   1-세로
    line, num = map(int, input().split())
    # 잘리는 좌표 i, j
    if line == 0:
        row.append(num)
        row.sort()
    else:
        col.append(num)
        col.sort()

result = []
for i in range(len(row)-1):
    for j in range(len(col)-1):
        x = row[i+1] - row[i]
        y = col[j+1] - col[j]
        result.append(x*y)

result.sort()
print(result.pop())


