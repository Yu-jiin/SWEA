switch_count = int(input())
switch_status = list(map(int, input().split()))
stu_num = int(input())
stu_list = [list(map(int, input().split())) for _ in range(stu_num)]

for st in stu_list:
    gender, number = st

    # 남
    if gender == 1:
        for i in range(number-1, switch_count, number):
            if switch_status[i] == 1:
                switch_status[i] = 0
            else:
                switch_status[i] = 1
    # print(switch_status)

    # 여
    else:
        if switch_status[number - 1] == 1:
            switch_status[number - 1] = 0
        else:
            switch_status[number - 1] = 1

        loop = min(number - 1, switch_count - number)

        for i in range(1, loop+1):
            if switch_status[number - 1 - i] == switch_status[number - 1 + i]:
                if switch_status[number - 1 - i] == 1:
                    switch_status[number - 1 - i] = 0
                else:
                    switch_status[number - 1 - i] = 1
                if switch_status[number - 1 + i] == 1:
                    switch_status[number - 1 + i] = 0
                else:
                    switch_status[number - 1 + i] = 1
            else:
                break

for i in range(1, switch_count+1):
    print(switch_status[i-1], end= " ")
    if i % 20 == 0:
        print()
