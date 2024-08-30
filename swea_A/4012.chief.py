import sys
sys.stdin = open('4012.txt')

def check_food(start, min_sum):
    for i in range(1, N):
        for j in range(1, N):
            if i == j:
                continue


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    padding = [0] * (N + 1)
    arr = [[0] + list(map(int, input().split())) for _ in range(N)]
    arr.insert(0, padding)

    min_food = float('inf')

    # 식재료 선택 경우의 수 만들기


    food1 = check_food(1, 0)
    food2 = check_food(1, 0)
