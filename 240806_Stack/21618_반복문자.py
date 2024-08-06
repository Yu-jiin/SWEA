T = int(input())
for tc in range(1, T+1):
    word = input()

    stack = []

    for w in word:
        if len(stack) == 0:  # 스택이 비어있으면 첫번째 값은 무조건 넣어주고 시작
            stack.append(w)
        else:
            # print(w, stack)
            if w != stack[-1]:
                stack.append(w)
            elif w == stack[-1]:
                stack.pop()
            if not stack:
                result = 0

    print(f'#{tc} {len(stack)}')