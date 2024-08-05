T = int(input())
for tc in range(1, T+1):
    person, submit = map(int, input().split())

    submit_lst = list(map(int, input().split()))

    origin = list(range(1, person+1))

    result = []

    for o in origin:
        if o not in submit_lst:
            result.append(o)

    result.sort()
    result = ' '.join(map(str, result))
    print(f'#{tc} {result}')