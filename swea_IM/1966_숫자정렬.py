T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    # # 버블정렬
    # for i in range(N-1, 0, -1):
    #     for j in range(i):
    #         if arr[j] > arr[j+1]:
    #             arr[j], arr[j+1] = arr[j+1], arr[j]
    #
    # result = ''.join(map(str, arr))
    # print(f'#{test_case} {result}')

    # # 선택정렬
    # for i in range(N):
    #     min_idx = i
    #     for j in range(i+1, N):
    #         if arr[j] < arr[min_idx]:
    #             min_idx = j
    #         arr[i], arr[min_idx] = arr[min_idx], arr[i]
    # #       i 인걸 잊지마라 제발 닥쳐
    #
    # result = ''.join(map(str, arr))
    # print(f'#{test_case} {result}')

    # 카운트 정렬
    max_value = max(arr)

    counts = [0] * (max_value + 1)
    temp = [0] * N

    # 각 숫자의 카운트 세주고
    for i in arr:
        counts[i] += 1

    # 카운트 누적합 계산 해주고
    for i in range(1, len(counts)):
        counts[i] += counts[i-1]

    # temp 채워주기
    for i in arr:
        temp[counts[i] - 1] = i
        counts[i] -= 1

    result = ' '.join(map(str, temp))
    print(f'#{test_case} {result}')

