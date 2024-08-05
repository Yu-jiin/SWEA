arr1 = [[1, 2, 3, 4, 5] for _ in range(5)]
print(arr1)

for i in range(5):
    for j in range(5):
        for k in range(j+1, 6):
            print(arr1[i][j+k])

