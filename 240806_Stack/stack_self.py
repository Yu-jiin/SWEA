T = int(input())
for tc in range(1, T+1):
    word = input()
    result = -1     # result -1 을 default 로
    stack = []
    if word[0] == '(':
        for w in word:
            # print(w, stack)
            if w == '(':
                stack.append(w)
            elif w == ')' and '(' == stack[-1]:
                stack.pop()
            elif w == ')':
                break
        if len(stack) == 0:
            result = 1

    print(f'#{tc} {result}')
