'''
3
1 3 5 7
0 5 2 4
0 5 1 6
'''

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    A = list(range(arr[0], arr[1]))
    B = list(range(arr[2], arr[3]))

    result = 0
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                result += 1
