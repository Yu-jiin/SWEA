# import sys
# sys.stdin = open('input.txt')

def dfs(idx, count):
    global result

    if int(change) == 1 and len(arr_list) == 2:
        arr_list.reverse()
        result = ''.join(arr_list)
        return

    if int(change) == 2 and len(arr_list) == 2:
        result = ''.join(arr_list)
        return

    if count == int(change):
        max_num = int(''.join(arr_list))
        # result = max(max_num, result)
        result = max(max_num, result)
        return

    for i in range(idx, len(arr_list)):
        for j in range(i+1, len(arr_list)):
            if arr_list[i] <= arr_list[j]:
                arr_list[i], arr_list[j] = arr_list[j], arr_list[i]
                dfs(i, count + 1)
                arr_list[i], arr_list[j] = arr_list[j], arr_list[i]

    if result == 0 and count < int(change):
        change2 = (int(change)-count) % 2
        if change2 == 1:
            arr_list[-1], arr_list[-2] = arr_list[-2], arr_list[-1]
        dfs(idx, int(change))


T = int(input())
for tc in range(1, T+1):
    arr, change = input().split()
    arr_list = []

    for a in arr:
        arr_list.append(a)

    result = 0
    dfs(0, 0)

    print(f'#{tc} {result}')

