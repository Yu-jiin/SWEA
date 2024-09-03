# arr = ['A', 'B', 'C', 'D', 'E']
# path = []
# n = 3
#
#
# def run(lev, start):
#     if lev == n:
#         print(*path)
#         return
#
#     for i in range(start, 5):
#         path.append(arr[i])
#         run(lev + 1, i + 1)
#         path.pop()
#
#
# run(0, 0)

# 규칙 - 선택할 수 있는 후보군들이 1씩 감소
#  ex)  5 * 4 * 3
#
# for i in range(5)             # N번을 뽑
#     for j in range(N+1, 5)    # M번 뽑
#         for k in range(M+1, 5)

#  이전에 뽑은거에서부터 시작

arr = ['1', '2', '3', '4', '5', '6']
path = []
n = 3


def run(lev, start):
    if lev == n:
        print(*path)
        return

    for i in range(start, 7):
        path.append(i)
        run(lev + 1, i)         # 중복이 가능
        path.pop()


run(0, 1)