T = int(input())
for test_case in range(1, T+1):
    tc = int(input())
    count = [0] * 5001

    for _ in range(tc):
        A, B = map(int, input().split())

        for i in range(A, B+1):
            count[i] += 1

    P = int(input())

    answer = []

    for _ in range(P):
        c = int(input())
        answer.append(count[c])

    result = ' '.join(map(str, answer))
    print(f'#{test_case} {result}')
