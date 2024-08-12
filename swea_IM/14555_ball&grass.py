T = int(input())
for tc in range(1, T+1):
    ground = input() + '0'
    # print(ground)
    stack = []
    count = 0

    for i in range(len(ground)-1):
        if ground[i] == "(" and ground[i+1] == "|":
            count += 1
        elif ground[i] == "(" and ground[i+1] == ")":
            count += 1
        elif ground[i] == "|" and ground[i+1] == ")":
            count += 1

    print(f'#{tc} {count}')