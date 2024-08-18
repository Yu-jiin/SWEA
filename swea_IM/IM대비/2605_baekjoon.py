N = int(input())
arr = list(map(int, input().split()))

stu = list(range(1, N+1))
new_stu = []

for i in range(N):
    new_stu.insert(arr[i], i+1)

new_stu.reverse()
print(*new_stu)
