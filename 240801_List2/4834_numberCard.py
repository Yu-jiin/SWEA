def counting_sort(arr):
    # 1. 배열에서 최대 값을 찾아 카운트 배열의 크기를 결정합니다.
    max_val = max(arr)  # 알고리즘으로는 배열의 크기를 결정해주니까

    # 2. 카운트 배열을 0으로 초기화합니다.
    count = [0] * (max_val + 1)

    # 3. 입력 배열의 각 값에 대해 카운트를 셉니다.
    for num in arr:
        count[num] += 1

    # 4. 카운트 배열을 수정하여 각 요소가 출력 배열에서 차지할 위치를 저장합니다.
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # 5. 출력 배열을 초기화합니다.
    output = [0] * len(arr)

    # 6. 입력 배열의 요소를 역순으로 순회하여 출력 배열에 올바른 위치에 배치합니다.
    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1

    # 7. 정렬된 요소를 원래 배열에 복사합니다.
    for i in range(len(arr)):
        arr[i] = output[i]


# 예시 사용법
arr = [4, 2, 2, 8, 3, 3, 1]
counting_sort(arr)
print(arr)  # 출력: [1, 2, 2, 3, 3, 4, 8]


# def counting_sort_most_frequent(cards):
#     # 카드에서 최대 값을 찾아서 카운트 배열의 크기를 결정합니다.
#     max_val = max(cards)
#
#     # 카운트 배열을 0으로 초기화합니다.
#     count = [0] * (max_val + 1)
#
#     # 각 카드의 숫자에 대한 빈도를 셉니다.
#     for card in cards:
#         count[card] += 1
#
#     # 가장 많이 등장한 숫자와 그 빈도를 찾습니다.
#     max_count = 0
#     most_frequent_card = 0
#     for i in range(len(count)):
#         if count[i] > max_count or (count[i] == max_count and i > most_frequent_card):
#             max_count = count[i]
#             most_frequent_card = i
#
#     return most_frequent_card, max_count
#
# # 예시 입력
# test_cases = [
#     (5, [49679, 34235, 56789, 34235, 34235]),
#     (10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]),
# ]
#
# # 각 테스트 케이스에 대해 결과를 출력합니다.
# for idx, (num_cards, cards) in enumerate(test_cases):
#     most_frequent_card, frequency = counting_sort_most_frequent(cards)
#     print(f"#{idx + 1} {most_frequent_card} {frequency}")
