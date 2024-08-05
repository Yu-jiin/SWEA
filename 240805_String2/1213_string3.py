T = 10
for test_case in range(1, T + 1):
    tc = int(input())
    word = input()
    s = input()

    lst = []
    count = 0
    for i in range(len(s) - len(word) + 1):
        if s[i:i + len(word)] == word:
            count += 1

    print(f'#{tc} {count}')
