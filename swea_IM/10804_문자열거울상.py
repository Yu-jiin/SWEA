T = int(input())


for tc in range(1, T+1):
    word = input()

    dic = {
        'b': 'd',
        'd': 'b',
        'p': 'q',
        'q': 'p'
    }

    reversed_word = word[::-1]

    result = ''
    for i in reversed_word:
        result += dic[i]

    print(f'#{tc} {result}')

