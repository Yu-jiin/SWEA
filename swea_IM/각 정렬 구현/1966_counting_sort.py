T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_value = max(arr)

    counts = [0] * (max_value + 1)
    temps = [0] * N

    for i in range(N):
        counts[arr[i]] += 1

    for i in range(1, max_value + 1):
        counts[i] += counts[i-1]

    for i in range(N-1, -1, -1):
        temps[counts[arr[i]] - 1] = arr[i]
        counts[arr[i]] -= 1

    result = ' '.join((map(str, temps)))
    print(f'#{tc} {result}')
