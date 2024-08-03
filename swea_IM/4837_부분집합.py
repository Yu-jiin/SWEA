T = int(input())  # 테스트 케이스의 수를 입력받음

for tc in range(1, T + 1):
    N, K = map(int, input().split())  # N: 부분집합의 원소 개수, K: 부분집합의 원소 합
    arr = list(range(1, 13))  # 1부터 12까지의 숫자 배열 생성
    subset_cnt = 2 ** 12  # 총 부분집합의 개수 (2^12 = 4096)

    subsets = []  # 모든 부분집합을 저장할 리스트

    # 모든 부분집합 생성
    for i in range(subset_cnt):
        subset = []
        for j in range(len(arr)):
            # i의 j번째 비트가 1이면 arr[j]를 부분집합에 포함
            if i & (1 << j):
                subset.append(arr[j])
        subsets.append(subset)  # 생성한 부분집합을 subsets 리스트에 추가

    counts = 0  # 조건을 만족하는 부분집합의 개수

    # 각 부분집합을 확인
    for idx in range(subset_cnt):
        # 부분집합의 합이 K이고, 부분집합의 원소 개수가 N인 경우
        if sum(subsets[idx]) == K and len(subsets[idx]) == N:
            counts += 1  # 조건을 만족하면 카운트를 증가

    print(f'#{tc} {counts}')  # 각 테스트 케이스의 결과를 출력
