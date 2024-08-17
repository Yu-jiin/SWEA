N, K = map(int, input().split())
arr = list(map(int, input().split())) + [0]

# 아오 시간 초과
# k = K-1
# sum_v = -250
# max_sum = -250
# for i in range(N):
#     sum_v = sum(arr[i:i+k])
#     if max_sum < sum_v:
#         max_sum = sum_v
#
# print(max_sum)

sum_v = [sum(arr[:K])]
for i in range(1, N-K+1):
    sum_v.append(sum_v[i-1] - arr[i-1] + arr[i + K - 1])

print(max(sum_v))

