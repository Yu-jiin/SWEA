T = int(input())
for tc in range(1, T+1):
    word = input()
    stack = []

    for w in word:
        if len(stack) == 0:
            stack.append(w)
        else:
            if w != stack[-1]:
                stack.append(w)
            elif w == stack[-1]:
                stack.pop()

    result = len(stack)
    print(f'#{tc} {result}')