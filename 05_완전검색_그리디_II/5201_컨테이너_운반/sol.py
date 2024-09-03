import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())        # N - 컨테이너 수  M - 트럭 수
    arr = list(map(int, input().split()))   # 화물 무게
    truck = list(map(int, input().split())) # 트럭 적재용량

    arr.sort()
    truck.sort()
    result = 0

    while truck:
        if truck and arr:
            if truck[-1] >= arr[-1]:
                truck.pop()
                result += arr.pop()
            else:
                arr.pop()
        else:
            break
            print(f'#{tc} {result}')

    print(f'#{tc} {result}')
