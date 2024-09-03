arr = ['A', 'B', 'C']
n = len(arr)


def get_sub(tar):
    for i in range(n):
        if tar & 0x1:
            print(arr[i], end='')
        tar >>= 1


for tar in range(0, 1 << n):  # range(0, 8)
    print('{', end='')
    get_sub(tar)
    print('}')

# 전체부분집합에서 => 최소 2명이상


def get_sub(tar):
    cnt = 0
    for i in range(n):
        if tar & 0x1:
            # print(arr[i], end='')
            cnt += 1
        tar >>= 1
    return cnt


for tar in range(0, 1 << n):  # range(0, 8)
    print('{', end='')
    get_sub(tar)
    print('}')