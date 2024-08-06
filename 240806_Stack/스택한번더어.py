T = int(input())
for tc in range(1, T+1):
    word = input()
    stack = []
    result = -1

    if word[0] == '(':
        for w in word:
            if w == '(':
                stack.append(w)
            elif w == ')' and stack[-1] == '(':
                stack.pop()
            elif w == ')':
                break
        if len(stack) == 0:
            result = 1

    print(f'#{tc} {result}')