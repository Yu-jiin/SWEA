Switch = int(input())   # 스위치 개수
switch_status = list(map(int, input().split()))     # 스위치 상태
stu_num = int(input())   # 학생 수


def main(Switch, stu_num):
    global switch_status

    for s in range(1, stu_num+1):
        gender, switch_num = map(int, input().split())

        if gender % 2 == 1:        # 남자일 때
            switch_range = Switch // switch_num     # 곱해줄 범위 정해주기
            for i in range(1, switch_range+1):
                if switch_status[(switch_num * i) - 1] == 1:
                    switch_status[(switch_num * i) - 1] = 0
                else:
                    switch_status[(switch_num * i) - 1] = 1

        if gender % 2 == 0:     # 여자일 때
            if switch_status[switch_num - 1] == 1:  # 스위치 번호는 즉시 바꿔주기
                switch_status[switch_num - 1] = 0
            else:
                switch_status[switch_num - 1] = 1
            if switch_num == 1 or switch_num == Switch:     # 스위치 번호가 1이거나 맨끝이면 건너뛰기 왜냐면 양옆으로 해줄 수 없으니
                continue
            else:   # 스위치 번호가 2부터 총 스위치 개수 -1 이라면
                for j in range(Switch // 2):    # 하나씩 넘어갈 범위 정해주기  j
                    if switch_num-2-j < 0 or switch_num+j >= Switch:    # 범위 넘어가는 순간 리턴
                        return
                    elif 0 <= switch_num-2-j < Switch and 0 <= switch_num+j < Switch:   # 범위내라면
                        if switch_status[switch_num-2-j] == switch_status[switch_num+j]:    # 만약 양옆이 같다면

                            if switch_status[switch_num - 2 - j] == 1:  # 양 옆 값 즉석 바꿔주기 
                                switch_status[switch_num - 2 - j] = 0
                            else:
                                switch_status[switch_num - 2 - j] = 1

                            if switch_status[switch_num + j] == 1:
                                switch_status[switch_num + j] = 0
                            else:
                                switch_status[switch_num + j] = 1
                        else:   # 양옆이 달라진다면
                            return  # 더 이상 계산하지 않고 바로 리턴 때리기


main(Switch, stu_num)

for i in range(0, len(switch_status), 20):
    a = switch_status[i: i+20]
    print(*a)


