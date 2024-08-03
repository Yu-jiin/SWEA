T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    # 5
    # 1 4 7 8 0
    # 배열 최대, 최소값 찾기 먼저 num 값 중에 음수가 있을 수도 있으니
    # max_value = max(num)
    # min_value = min(num)
    # r = max_value - min_value + 1
    #
    # counts = [0] * r
    # temp = [0] * N
    #
    # for i in range(N):
    #     counts[num[i] - min_value] += 1
    #
    # for i in range(1, r):
    #     counts[i] += counts[i - 1]
    #
    # for i in range(N-1, -1, -1):
    #     temp[counts[num[i] - min_value] - 1] = num[i]
    #     counts[num[i] - min_value] -= 1
    #
    # result = ' '.join(map(str, temp))
    # print(f'#{tc} {result}')

    # 양수만 있는 전형적인 카운팅 정렬
    # 카운팅 정렬을 위한 준비
    # max_value = max(arr)  # 배열의 최대값을 찾음
    # range_of_elements = max_value + 1  # 요소 범위
    #
    # count = [0] * range_of_elements  # 카운트 배열
    # output = [0] * N  # 출력 배열
    #
    # # 각 숫자의 개수를 카운트
    # for i in range(N):
    #     count[arr[i]] += 1
    #
    # # 누적합 계산
    # for i in range(1, range_of_elements):
    #     count[i] += count[i - 1]
    #
    # # 출력 배열을 채움
    # for i in range(N - 1, -1, -1):
    #     output[count[arr[i]] - 1] = arr[i]
    #     count[arr[i]] -= 1
    #
    # # 결과 출력
    # print(f'#{tc}', ' '.join(map(str, output)))

    
    # 버블 정렬
    # 인접한 두개 서로 바꾸기
    # for i in range(N-1, 0, -1):
    #     for j in range(i):
    #         if num[j] > num[j+1]:
    #             num[j], num[j+1] = num[j+1], num[j]
    #
    # result = ' '.join(map(str, num))
    # print(f'#{tc} {result}')
    #
    # for i in range(N-1, 0, -1):
    #     for j in range(i):
    #         if num[j] > num[j+1]:
    #             num[j], num[j+1] = num[j+1], num[j]
    #
    # result = ' '.join(map(str, num))
    # print(result)

    # 선택정렬
    for i in range(N):
        min_idx = i
        for j in range(i+1, N):
            if num[j] < num[min_idx]:
                min_idx = j
        num[i], num[min_idx] = num[min_idx], num[i]

