import sys
sys.stdin = open('5656.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    # N - 구슬 떨군 횟수      W * H 배열
    N, W, H = list(map(int, input().split()))
    arr = [list(map(int, input())) for _ in range(W)]
    