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

    return result


def calcu(result):
    total = 0


T = 10
for tc in range(1, T+1):
    str_len = int(input())
    postfix = list(map(str,input()))

    print(make_postfix(postfix))
