import sys
sys.stdin = open('input.txt')  # 표준 입력을 'input.txt' 파일로부터 읽어옵니다.

def dfs(idx, count):
    global result

    # 기저 사례: 교환 횟수가 1이고 arr_list의 길이가 2일 때, 리스트를 역순으로 바꿉니다.
    if int(change) == 1 and len(arr_list) == 2:
        arr_list.reverse()
        result = ''.join(arr_list)  # 리스트를 문자열로 변환하고 결과에 저장합니다.
        return

    # 기저 사례: 교환 횟수가 2이고 arr_list의 길이가 2일 때, 리스트를 문자열로 변환하고 결과에 저장합니다.
    if int(change) == 2 and len(arr_list) == 2:
        result = ''.join(arr_list)  # 리스트를 문자열로 변환하고 결과에 저장합니다.
        return

    # 현재 교환 횟수가 허용된 교환 횟수와 같으면, 현재의 숫자 문자열을 결과와 비교합니다.
    if count == int(change):
        max_num = int(''.join(arr_list))  # 리스트를 문자열로 변환하여 정수로 변환합니다.
        result = max(max_num, result)  # 결과와 비교하여 더 큰 값을 저장합니다.
        return

    # 교환을 수행합니다.
    for i in range(idx, len(arr_list)):
        for j in range(i+1, len(arr_list)):
            if arr_list[i] <= arr_list[j]:  # arr_list[i]가 arr_list[j]보다 작거나 같을 때만 교환합니다.
                arr_list[i], arr_list[j] = arr_list[j], arr_list[i]  # 교환
                dfs(i, count + 1)  # 교환한 후 다음 단계로 재귀 호출
                arr_list[i], arr_list[j] = arr_list[j], arr_list[i]  # 교환을 원래대로 되돌립니다.

    # 교환 횟수가 남아있고 결과가 아직 0이라면, 마지막 두 원소를 교환할 수 있는지 확인합니다.
    if result == 0 and count < int(change):
        change2 = (int(change) - count) % 2
        if change2 == 1:
            arr_list[-1], arr_list[-2] = arr_list[-2], arr_list[-1]  # 마지막 두 원소를 교환합니다.
        dfs(idx, int(change))  # 남은 교환 횟수로 재귀 호출

# 테스트 케이스 수를 읽습니다.
T = int(input())
for tc in range(1, T + 1):
    arr, change = input().split()  # 숫자 문자열과 교환 횟수를 입력받습니다.
    arr_list = []

    for a in arr:
        arr_list.append(a)  # 문자열을 리스트로 변환합니다.

    result = 0  # 결과를 초기화합니다.
    dfs(0, 0)  # 깊이 우선 탐색을 시작합니다.

    print(f'#{tc} {result}')
