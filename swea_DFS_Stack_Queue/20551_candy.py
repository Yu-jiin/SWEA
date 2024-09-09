import sys
sys.stdin = open('20551.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    A, B, C = map(int, input().split())
    candy = 0

    if A > B > C:
        print(f'#{tc} -1')

    elif A < B < C:
        print(f'#{tc} 0')

    elif C <= B:
        B -= 1
        candy += 1
        if B <= A:
            A -= 1
            candy += 1
            print(f'#{tc} {candy}')
        else:
            print(f'#{tc} {candy}')



