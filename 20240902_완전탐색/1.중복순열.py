# path = []
#
#
# def kfc(x):
#     if x == 3:
#         print(path)
#         return
#
#     for i in range(1, 7):
#         path.append(i)
#         kfc(x + 1)
#         path.pop()
#
#
# kfc(0)


result1 = []


def permutation2(x):
    if x == 5:
        print(result1)
        return

    for i in range(1, 5):
        result1.append(i)
        permutation2(x + 1)
        result1.pop()


permutation2(0)