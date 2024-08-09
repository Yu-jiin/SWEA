def f(i, k, s, t):  # i-원소  k-집합의 크기  s-i-1까지 고려된 합  t-목표
    global cnt
    global fcnt
    fcnt += 1
    if i == k:  # 모든 원소 고려 밑에 가지치기 파트도 한번 보자
        if s == t:
            print(bit)
            cnt += 1
        return
    else:
        bit [i] = 1
        f(i+1, k, s + A[i], t)  # A[i] 포함
        bit[i] = 0
        f(i+1, k, s, t)     # A[i] 미퍼힘


A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = 10
# A = [i for i in range(1, N + 1)]

key = 10
cnt = 0
bit = [0] * N
fcnt = 0
f(0, N, 0, key)


    # 가지치기 경우
    # if s > t:
    #     return
    # elif s == t:
    #     ctn += 1
    #     return
    # elif i == k:
    #     return
