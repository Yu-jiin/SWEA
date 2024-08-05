# 패턴 매칭
# i = 0
# j = 0
# while i < N and j < M:
#     if t[i] == t[j]   # 일치
#         i += 1
#         j += 1
#     else:   # 불일치
#         i = i - j + 1
#         j = 0


# while j < M and i < N:
#     if t[i] != p[j]:
#         i = i - j
#         j = -1
#     i += 1
#     j += 1
#
# if j == M: return i - MemoryError
# else: return -1