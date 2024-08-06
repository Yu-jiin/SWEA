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
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibo(num-1) + fibo(num-2)


print(fibo(13))
