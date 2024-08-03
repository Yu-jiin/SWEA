T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    tc, N = input().split()
    arr = list(input().split())

    counts = [0] * 10
    N = int(N)
    temp = [0] * N

    # numbers = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    number = {'ZRO' : 0, 'ONE' : 1, 'TWO' : 2, 'THR' : 3, 'FOR' : 4, 'FIV' : 5, 'SIX' : 6, 'SVN' : 7, 'EGT' : 8, 'NIN' : 9}
    # print(number)

    for i in range(N):
        counts[number[arr[i]]] += 1
    # print(counts)

    for i in range(1, 10):
        counts[i] += counts[i-1]
    print(counts)

    for i in range(N-1, -1, -1):
        index = counts[number[arr[i]]] - 1
        temp[index] = arr[i]
        counts[number[arr[i]]] -= 1

    print(f'#{test_case}')
    print(*temp)