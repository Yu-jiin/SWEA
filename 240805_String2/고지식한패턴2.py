# def f(t, p):
#     N = len(t)
#     M = len(p)
#
#     for i in range(N - M + 1):  # 비교구간의 시작위치
#         for j in range(M):
#             if t[i + j] != p[j]:
#                 break  # for j, 다음 글자부터 비교 시작
#         else:  # for j가 중단없이 반복되면
#             return i  # 패턴을 찾은 경우
#     return -1
#
# t = 'TTTTTATTTAATA'
# p = 'TTA'


