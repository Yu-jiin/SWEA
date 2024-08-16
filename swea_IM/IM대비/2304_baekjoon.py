N = int(input())
height = [0] * 15
for _ in range(1, N+1):
    L, H = map(int, input().split())
    # L = 기둥 위치
    # H = 높이
    height[L-1] = H
    max_v = max(height)

    for h in range(len(height)):
        if height[h] == max_v:
            middle = h
