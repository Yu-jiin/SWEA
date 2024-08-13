# 큐의 기본 연산
# 삽입 : enQueue(item)
# 삭제 : deQueue()
# 생성 : createQueue()
# 삭제 없이 반환 : Qpeek()
# 공백인지 확인 : isEmpty()
# 포화인지 확인 : isFull()
# 초기상태 = front = rear = -1
# 공백상태 = front == rear
# 포화상태 = rear == n-1
# 초기 공백 큐 생성
# 크기 n 인 1차원 배열 생성, front rear -1로 초기화

N = 10
q = [0] * N
front = -1
rear = -1

rear += 1       # enqueue(1)
q[rear] = 1
rear += 1
q[rear] = 2     # enqueue(2)
rear += 1
q[rear] = 3     # enqueue(3)

front += 1
print(q[front])
front += 1
print(q[front])

print(q)
