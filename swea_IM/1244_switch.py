Switch = int(input())   # 스위치 개수
switch_status = list(map(int, input().split()))     # 스위치 상태
stu_num = int(input())   # 학생 수


def main(Switch, stu_num):
    global switch_status

    for s in range(1, stu_num+1):
        gender, switch_num = map(int, input().split())

        if gender % 2 == 1:
            switch_range = Switch // switch_num
            for i in range(1, switch_range+1):
                if switch_status[(switch_num * i) - 1] == 1:
                    switch_status[(switch_num * i) - 1] = 0
                else:
                    switch_status[(switch_num * i) - 1] = 1

        if gender % 2 == 0:
            if switch_status[switch_num - 1] == 1:
                switch_status[switch_num - 1] = 0
            else:
                switch_status[switch_num - 1] = 1
            if switch_num == 1 or switch_num == Switch:
                continue
            else:
                for j in range(Switch // 2):
                    if switch_num-2-j < 0 or switch_num+j >= Switch:
                        return
                    elif 0 <= switch_num-2-j < Switch and 0 <= switch_num+j < Switch:
                        if switch_status[switch_num-2-j] == switch_status[switch_num+j]:

                            if switch_status[switch_num - 2 - j] == 1:
                                switch_status[switch_num - 2 - j] = 0
                            else:
                                switch_status[switch_num - 2 - j] = 1

                            if switch_status[switch_num + j] == 1:
                                switch_status[switch_num + j] = 0
                            else:
                                switch_status[switch_num + j] = 1
                        else:
                            return


main(Switch, stu_num)

for i in range(0, len(switch_status), 20):
    a = switch_status[i: i+20]
    print(*a)


