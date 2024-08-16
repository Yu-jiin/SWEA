n = int(input())
max_list = []  # 뽑은 수 저장 리스트
max_len = 0  # 최대 개수의 수

for j in range(1, n + 1):
    lst = [n, j]
    i = 0

    while True:
        a = lst[i] - lst[i + 1]
        i += 1
        if a < 0:
            break
        lst.append(a)

    if max_len < len(lst):
        max_len = len(lst)
        result = lst[:]

print(max_len)
print(*result)
