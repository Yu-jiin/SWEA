T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split())) + [0]

    up_list = []
    up = [arr[0]]   # 제일 처음 요소를 미리 넣음
    for i in range(N):
        # 현재 숫자와 비교하여 다음 숫자가 작은 경우, 리스트 안이 초기화 되기에 현재 요소 값 넣어주기
        if up == []:
            up.append(arr[i])
        if arr[i] <= arr[i + 1]:
            up.append(arr[i+1])
        else:
            up_list.append(up)
            up = []

        # print(up)

    new_list = []
    for inner in up_list:
        min_v = inner[0]
        max_v = inner[-1]

        if len(inner) == 1: continue

        length = len(inner)

        avg = (max_v - min_v) // len(inner)

        new_list.append(([length, avg]))