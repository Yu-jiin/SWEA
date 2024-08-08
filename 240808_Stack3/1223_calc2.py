def postfix(arr):
    result = ''
    stack = []
    dic = {
        '*': 2, '/': 2,
        '+': 1, '-': 1
    }
    for n in arr:
        if n.isdigit():
            result += n
        elif n in dic:
            if stack and dic[stack[-1]] >= dic[n]:
                result += stack.pop()
            stack.append(n)

    while stack:
        result += stack.pop()

    return calc(result)


def calc(result):
    stack = []
    for r in result:
        if r.isdigit():
            stack.append(r)
        else:
            first = stack.pop()
            end = stack.pop()
            if r == '+':
                stack.append(int(first) + int(end))
            elif r == '*':
                stack.append(int(first) * int(end))
            elif r == '/':
                stack.append(int(first) // int(end))
            else:
                stack.append(int(first) - int(end))

    return stack.pop()


T = 10
for tc in range(1, T+1):
    l = int(input())
    arr = list(map(str, input()))

    total_result = postfix(arr)
    print(f'#{tc} {total_result}')
