# import sys
# sys.stdin = open('input.txt')

# 13
# 1 2 1 3 2 4 3 5 2 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

# left, right 쓰는 버전
# 단, 입력이 반드시 각 노드당 최대 2번씩만 들어온다고 가정한 코드
N = int(input())
arr = list(map(int, input().split()))

left = [0] * (N+1)      # 왼쪽 번호 저장 리스트
# ex) left[3] = 2 ==> 3번 부모의 왼쪽 자식은 2다

right = [0] * (N+1)     # 오른쪽 번호 저장 리스트

for i in range(0, len(arr), 2):
    parent, child = arr[i], arr[i+1]
    
    # 왼쪽 자식이 없다면, 왼쪽에 삽입
    if left[parent] == 0:
        left[parent] = child
    # 왼쪽 자식은 있는데, 오른쪾 자식이 없다면
    else:
        right[parent] = child

print(left)
print(right)