T = 10
for tc in range(1, T+1):
    num, word = list(map(str, input().split()))
    # print(num, word)
    stack = []
    for w in word:
        # print(stack, w)
        if len(stack) == 0:
            stack.append(w)
        else:
            if w != stack[-1]:
                stack.append(w)
            elif w == stack[-1]:
                stack.pop()

    result = ''.join(stack)
    print(f'#{tc} {result}')
