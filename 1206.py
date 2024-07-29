
# 10
# 0 0 254 185 76 227 84 175 0 0
# 출력값 = 111
T = int(input())
for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0
    for i in range(1, N):
        if arr[i] > arr[i-2] and arr[i] > arr[i-1] and arr[i] > arr[i+1] and arr[i] > arr[i+2]:
            max_v = max(arr[i-1], arr[i-2], arr[i+1], arr[i+2])
            a = arr[i] - max_v
            result += a

    print(f'#{tc} {result}')

