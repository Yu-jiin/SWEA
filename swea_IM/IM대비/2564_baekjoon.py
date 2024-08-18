# 경비원
N, M = map(int, input())
C = int(input())
for _ in range(C):
    A, B = map(int, input().split())    # 상점 위치

X, Y = map(int, input())
where = [1, 2, 3, 4]
# 1-북 2-남 3-서 4-동
# 동근이가 북 남에 있을 때
for i in where:
    if A == i:
        pass



