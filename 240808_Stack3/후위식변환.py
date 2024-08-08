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
        elif postFix[n] in dic:
            while stack and stack[-1] in dic and dic[stack[-1]] >= dic[postFix[n]]:
                result.append(stack.pop())
            stack.append(postFix[n])

    while stack:
        result.append(stack.pop())

    answer = ''.join(result)
    print(f'#{tc} {answer}')


