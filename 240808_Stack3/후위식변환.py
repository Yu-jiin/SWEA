T = int(input())
for tc in range(1, T + 1):
    postFix = list(map(str, input()))
    # print(postFix)
    dic = {
        '*': 2, '/': 2,
        '+': 1, '-': 1
    }
    result = []
    stack = []

    for n in range(len(postFix)):
        if postFix[n].isdigit():
            result.append(postFix[n])
        elif n in dict:
            if stack and dic[stack[-1]] >= dic[n]:
                result.append(stack.pop())
            stack.append(n)

    while stack:
        result.append(stack.pop())

    print(' '.join(result))


