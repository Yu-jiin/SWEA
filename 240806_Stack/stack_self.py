T = int(input())
for tc in range(1, T+1):
    word = input()

    stack = []

    for w in word:
        if w is '(':
            stack.append(w)
        elif w is ')':
            if not stack or stack[-1] == '(':   # ?
                stack.pop()
            result = -1
        if len(stack) == 0:
            result = 1
