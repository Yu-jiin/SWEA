import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    max_row = 0
    for row in arr:
        if max_row < len(row):
            max_row = len(row)

    for row in arr:
        while len(row) < max_row:
            row.append(0)

    for col in zip(*arr):
        pass


    for i in range(len(col)):
        for j in range(1, len(col)):