def f(n):
    global cnt
    cnt += 1
    if n == 0:
        return
    else:
        f(n-1)


cnt = 0
f(50)   # 파이파이는 1000번대도 가능 ㅠㅠ
print(cnt)


# 팩토리얼
def fac(num):
    if num == 1:
        return 1
    else:
        return num * fac(num - 1)
    # num * fac(num-1)


print(fac(5))


# 피보나치
def fibo(num):
    if num == 0:    # if num < 2: return n
        return 0
    elif num == 1:
        return 1
    else:
        return fibo(num-1) + fibo(num-2)


print(fibo(13))
