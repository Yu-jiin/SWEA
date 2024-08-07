# 메모이제이션으로 피보나치 풀어보기
def fibo(n):
    f = [0] * (n+1)     # 0으로 초기화 시켜서 배열 만들기
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]

    return f[n]


print(fibo(7))
