def check_arr(arr):
    stack = []
    dic = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    for a in arr:
        # print(stack)
        if a in dic.values():
            stack.append(a)
        elif a in dic.keys():
            if stack[-1] != dic[a] or not stack:
                return False
            # if 문이 아니라면 제거해서 ㅃ ㅐ
            stack.pop()
    return not stack


T = int(input())
for tc in range(1, T+1):
    arr = input()
    result = check_arr(arr)

    if result is True:
        result = 1
    else:
        result = 0

    print(f'#{tc} {result}')
