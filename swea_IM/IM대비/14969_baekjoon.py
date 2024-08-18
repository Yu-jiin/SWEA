N = int(input())

for _ in range(N):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = 'D'
    a = A.pop(0)
    b = B.pop(0)

    A4 = A.count(4)     # A 별 개수
    B4 = B.count(4)     # B 별 개수
    A3 = A.count(3)
    B3 = B.count(3)
    A2 = A.count(2)
    B2 = B.count(2)
    A1 = A.count(1)
    B1 = B.count(1)

    if A4 > B4:
        result = 'A'
    elif A4 < B4:
        result = 'B'
    elif A3 > B3:
        result = 'A'
    elif A3 < B3:
        result = 'B'
    elif A2 > B2:
        result = 'A'
    elif A2 < B2:
        result = 'B'
    elif A1 > B1:
        result = 'A'
    elif A1 < B1:
        result = 'B'

    print(result)