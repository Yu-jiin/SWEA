N = int(input())
arr = list(map(int, input().split()))
arr.append(0)
# 오르막
new_list = [arr[0]]
max_len = 0

for i in range(1, N):
    if arr[i] > arr[i-1]:
        new_list.append(arr[i])
    else:
        new_list = [arr[i]]

    up = new_list[-1] - new_list[0]
    if max_len < up:
        max_len = up

print(max_len)
