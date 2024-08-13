# 원형큐
# 1차원 배열 사용하되, 논리적으로는 배열의 처음과 끝이 연결되어
# 원형 형태의 큐를 이룬다고 가정

# 초기 공백 상태
# front = rear = 0

# index의 순환
# front와 rear의 위치가 배열의 마지막 인덱스인 n-1를 가르킨 후
# 그 다음에 논리적 순환을 이루어 배열의 처음 인덱스 0으로 이동해야함
# 이를 위해 나머지 연산자 mod 사용

# front 변수
# 공백 상태와 포화 상태 구분을 쉽게 하기 위해 front 가 있는 자리는 사용하지 않고 빈자리로
#
# rear = (rear + 1)mod n    삽입
# front = (front + 1)mod n  삭제

# cQ = 4
# Q_SIZE = 4
# front = rear = 0
#
# rear = (rear + 1) % Q_SIZE   # enq(1)
# cQ[rear] = 1
#
# rear = (rear + 1) % Q_SIZE   # enq(2)
# cQ[rear] = 2
#
# rear = (rear + 1) % Q_SIZE   # enq(3)
# cQ[rear] = 3
#
# front = (front + 1) % Q_SIZE
# print(cQ[front])
#
# front = (front + 1) % Q_SIZE
# print(cQ[front])
#
# front = (front + 1) % Q_SIZE
# print(cQ[front])


# list_q = []
# for i in range(10000):
#     list_q.append(i)
# for _ in range(1000):
#     list_q.pop(0)
# print('end')

from collections import deque
deque_q = deque()
for i in range(10000):
    deque_q.append(i)
for _ in range(100):
    deque_q.popleft()
print('end')