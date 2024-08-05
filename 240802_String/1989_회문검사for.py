T = int(input())
for tc in range(1, T+1):
    word = input()

    l = len(word)

    for i in range(l // 2):
        # print(word[l-1-i], word[i])
        if word[i] == word[l - 1 - i]:
            result = 1
        else:
            result = 0

    print(f'#{tc} {result}')