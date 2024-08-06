def stack(word):
    stack = []
    result = -1
    for w in word:
        if w == '(':
            stack.append(w)
        elif w == ')':
            if not stack:
                return result
            stack.pop()

    if len(stack) == 0:
        result = 1
    return result


T = int(input())
for tc in range(1, T+1):
    word = input()
    print(f'#{tc} {stack(word)}')