import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    times = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    count = 0
    hours = list(range(1, 25))
    print(times)

    for i in range(N):
        for j in range(2):
            time = abs(i-j)

    # for i in range(s, e):
    #     if i in hours:
    #         hours.remove(i)
    #         result += 1
    #         if result == len(range(s, e)):
    #             count += 1
    #             result = 0
    #     else:
    #         result = 0
    #         break

    print(f'#{tc} {count}')