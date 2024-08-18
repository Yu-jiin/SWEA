N, K = map(int, input().split())
stu = [[0]*6 for _ in range(2)]
room = 0
for _ in range(N):
    gender, grade = map(int, input().split())
    stu[gender][grade-1] += 1

for i in stu:
    for j in i:
        if j % K == 0:
            room += j//K
        else:
            room += (j//K) + 1
print(room)

