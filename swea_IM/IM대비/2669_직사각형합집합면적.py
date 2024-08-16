arr = [[0]*101 for _ in range(101)]

for _ in range(4):
    a, b, c, d = map(int, input().split())

    for i in range(b+1, d+1):
        for j in range(a+1, c+1):
            arr[i][j] = 1

    count = 0
    for i in range(101):
        for j in range(101):
            if arr[i][j] == 1:
                count += 1

# print(arr)
print(count)
