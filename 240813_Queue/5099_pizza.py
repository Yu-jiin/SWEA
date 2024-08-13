T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    array = list(map(int, input().split()))
    # 화덕 한바퀴 돌 때 녹지않은 치즈의 양은 반으로
    # stack = []
    index_pizza = list(enumerate(array, start=1))
    # print(index_pizza)
    # for pizza_num in enumerate(array, start=1):
    stack = index_pizza[:N]
    remain = index_pizza[N:]

    # while len(stack) > 1:
    #     for i in range(N):
    #         i = 0
    #         stack.append(stack[i] // 2)
    #         stack.pop(0)
    #         if stack[i] == 0:
    #             stack.pop(0)
    #             if N+1 <= M:
    #                 stack.append(remain.pop(0))
    #                 N += 1

    while len(stack) > 1:
        c = stack.pop(0)
        if c[1]//2 != 0:
            c[1] = c[1] // 2
            stack.append(c)
        else:
            if remain:
                stack.append(remain.pop(0))

    print(f'#{tc} {stack[0][0]}')
