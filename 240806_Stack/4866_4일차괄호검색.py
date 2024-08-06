def check(code):
    stack = []
    dic = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    for c in code:
        # print(stack) 여기에 프린트 찍으면 스택변화 실시간 확인 가능 최박사님 최고
        if c in dic.values():
            stack.append(c)
        elif c in dic.keys():
            if not stack or stack[-1] != dic[c]:
                return False
            stack.pop()
    return not stack
    stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False


T = int(input())
for tc in range(1, T+1):
    code = input()

    result = check(code)
    if result is True:
        result = 1
    else:
        result = 0

    print(f'#{tc} {result}')