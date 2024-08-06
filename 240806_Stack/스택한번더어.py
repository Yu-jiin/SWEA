T = int(input())
for tc in range(1, T+1):
    word = input()
    stack = []
    result = -1

    for w in word:
        if w == '(':
            stack.append(w)
        elif w == ')':  # 괄호 닫힐때,
            if not stack:
                # result = -1
                break
            stack.pop()
    else:
        if len(stack) == 0:
            result = 1

    print(f'#{tc} {result}')

