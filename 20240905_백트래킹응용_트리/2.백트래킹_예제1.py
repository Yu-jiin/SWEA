# 1,2,3,4,5,6,7,8,9,10}의 powerset 중 원소의 합이 10인 부분집합을 모두 출력하시오.
arr = [i for i in range(1, 11)]
visited = []


def dfs(level, sum):
    if level == len(arr):
        return
    # 기저조건
    if sum > 10:
        return
    # 기저조건 - 문제에서 발견하기 힘든 경우 다수
    if sum == 10:
        print(*visited)
        return

    for i in range(len(arr)):
        # 가지치기 : 이미 사용한 숫자라면 생략쓰
        if arr[i] in visited:
            continue

        visited.append(arr[i])
        dfs(level + 1, sum + arr[i])
        visited.pop()


dfs(0, 0)