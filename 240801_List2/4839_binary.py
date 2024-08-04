T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    #
    # def search(target, P):
    #     start = 1
    #     end = P
    #     count = 0
    #     while start <= end:
    #         count += 1
    #         middle = (start + end)//2
    #         if middle == target:
    #             return count
    #         if middle > target:
    #             end = middle
    #         else:
    #             start = middle
    #     return count
    #
    # resultA = search(A, P)
    # resultB = search(B, PP, A, B = map(int, input().split()))
    #
    # if resultA < resultB:
    #     result = 'A'
    # elif resultA > resultB:
    #     result = 'B'
    # else:
    #     result = 0
    #
    # print(f'#{test_case} {result}')




#  self
    P, A, B = map(int, input().split())

    def search(target, P):
        start = 1
        end = P
        count = 0

        while start <= end:
            count += 1
            middle = (start + end) // 2
            if middle == target:
                return count
            if middle > target:
                end = middle
            else:
                start = middle
            return count

    countA = search(A, P)
    countB = search(B, P)

    if countA < countB:
        result = 'A'
    elif countB < countA:
        result = 'B'
    else:
        result = 0

    print(f'#{test_case} {result}')