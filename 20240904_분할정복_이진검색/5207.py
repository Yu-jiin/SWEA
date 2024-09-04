T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    find = list(map(int, input().split()))
    cnt = 0
    lst.sort()

    low = 0
    high = len(lst) - 1
    # flag
    while low <= high:


    print(f'#{tc} {cnt}')