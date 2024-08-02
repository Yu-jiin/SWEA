T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    tc, N = input().split()
    leng = int(N)
    # print(leng)
    arr = list(input().split())
    # print(arr)
    counts = [0] * 10
    temp = [0] * leng

    numbers = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX']

    # 그냥 딕셔너리 만드는건 어떠니 지인아 ?ㅓㅂ ㅕㅇ신같은 짓 그만두고
    for x in arr:
        if x == 'ZRO':
            counts[0] += 1
        if x == 'ONE':  # 이렇게 하고싶으면 elif
            counts[1] += 1
        if x == 'TWO':
            counts[2] += 1
        if x == 'THR':
            counts[3] += 1
        if x == 'FOR':
            counts[4] += 1
        if x == 'FIV':
            counts[5] += 1

    print(counts)

