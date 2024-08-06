def f2(c, d):
    return c - d


def f1(a, b):
    c = a + b
    d = 10
    return f2(c, d)


a = 10
b = 20
print(f1(a, b))


def f2(d, c):   # c가 c를 받는 것이 아닌 들어온 순서대로 받기에
    return d - c    # d = 30   c = 10


def f1(b, a):  # b = 10, a = 20, c = 30
    c = a + b
    d = 10
    return f2(c, d)     # c =  30, d = 10


a = 10
b = 20
print(f1(a, b))

