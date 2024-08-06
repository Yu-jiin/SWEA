def check(code):
    stack = []
    match = {')': '('}
    for c in code:
        if c in match.values():
            stack.append(c)
        elif c in match.keys():
            if not stack or stack[-1] != match[c]:
                return False
            stack.pop()
    return not stack    # 모든 문자를 순회한 후 스택이 비어 있으면 True 반환, 그렇지 않으면 False 반환
    stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False


T = int(input())
for tc in range(1, T+1):
    code = input()
    # print(check(code))
    result = check(code)
    if result is True:
        result = 1
    else:
        result = -1

    print(f'#{tc} {result}')



