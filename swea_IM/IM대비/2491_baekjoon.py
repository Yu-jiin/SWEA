N = int(input())
arr = list(map(int, input().split()))

plus = [arr[0]]
minus = [arr[0]]
max_len = 1
for i in range(1, N):
    # plus
    if arr[i] > arr[i-1]:
        plus.append(arr[i])
        minus = [arr[i]]
    # minus
    elif arr[i] < arr[i-1]:
        minus.append(arr[i])
        plus = [arr[i]]
    else:
        plus.append(arr[i])
        minus.append(arr[i])

    max_len = max(max_len, len(plus), len(minus))

print(max_len)



