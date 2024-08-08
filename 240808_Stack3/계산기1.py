def make_postfix(postfix):
    result = ''
    stack = []
    t = {
        '+': 1
    }
    for n in postfix:
        if n.isdigit():
            result += n
        elif n in t.keys():
            if stack:
                result += stack[-1]
                stack.pop()
            stack.append(n)

    while stack:
        result += stack[-1]
        stack.pop()

    return calcu(result)


def calcu(result):
    total = 0
    stack = []

    for n in result:
        if n.isdigit():
            stack.append(n)
        else:
            first = stack.pop()
            end = stack.pop()
            sum_v = int(first) + int(end)
            stack.append(sum_v)
    while stack:
        total = stack.pop()

    return total

T = 10
for tc in range(1, T+1):
    str_len = int(input())
    postfix = list(map(str,input()))

    answer = make_postfix(postfix)
    print(f'#{tc} {answer}')
