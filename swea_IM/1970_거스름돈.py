T = int(input())
for tc in range(1, T+1):
    money = int(input())
    lst = [0 for i in range(8)]
    while money != 0:
        if money >= 50000:
            lst[0] += 1
            money = money - 50000
            # print(lst[0])
        elif money >= 10000:
            lst[1] += 1
            money = money - 10000
            # print(lst[1])
        elif money >= 5000:
            lst[2] += 1
            money = money - 5000
            # print(lst[2])
        elif money >= 1000:
            lst[3] += 1
            money = money - 1000
            # print(lst[3])
        elif money >= 500:
            lst[4] += 1
            money = money - 500
        elif money >= 100:
            lst[5] += 1
            money = money - 100
        elif money >= 50:
            lst[6] += 1
            money = money - 50
        elif money >= 10:
            lst[7] += 1
            money = money - 10

    print(f'#{tc}')
    print(*lst)
