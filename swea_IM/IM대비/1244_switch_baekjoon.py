N = int(input())    # 스위치 개수
switch_list = list(map(int, input().split()))
loops = 0
stu_N = int(input())
for _ in range(stu_N):
    gender, num = map(int, input().split())

    if gender == 1:
        for i in range(num-1, N, num):
            if switch_list[i] == 1:
                switch_list[i] = 0
            else:
                switch_list[i] = 1
    # 여자일 때
    else:
        if switch_list[num-1] == 1:
            switch_list[num-1] = 0
        else:
            switch_list[num-1] = 1

        loops = min(num-1, N-num)

        for l in range(1, loops+1):
            if switch_list[num-1-l] == switch_list[num-1+l]:
                if switch_list[num - 1 - l] == 1:
                    switch_list[num - 1 - l] = 0
                else:
                    switch_list[num - 1 - l] = 1
                if switch_list[num - 1 + l] == 1:
                    switch_list[num - 1 + l] = 0
                else:
                    switch_list[num - 1 + l] = 1
            else:
                break

for i in range(1, N+1):
    print(switch_list[i-1], end= " ")
    if i % 20 == 0:
        print()
