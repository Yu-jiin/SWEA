# 큐 삽입
# rear 값을 하나 증가시켜 새로운 원소를 삽입할 자리를 마련
# 그리고 그 인덱스에 해당하는 배열원서 Q[rear]에 item 저장

# def enQueue(item):
#     global rear
#     rear += 1
#     Q[rear] = item

# 큐 삭제
# front 값을 증가시켜 큐에 남아있는 첫 번째 원소 이동
# 새로운 첫 번째 원소 리턴
# deQueue()
#     front += 1
#     return Q[front]


# 공백, 포화 상태 검사
# 공백 : front == rear
# 포화 : rear == n-1 (n : 배열의 크기, n-1 : 배열의 마지막 인덱스)
# def is Empty():
#     return front == rear
# 
# def isFull():
#     return rear == len(Q)-1


# 큐 검색 Qpeek()
# 가장 앞에 있는 원소를 검색하여 반환
# 현재 front의 한자리 뒤에 있는 원소, 즉 큐의 첫번째 원소를 반환
# def Qpeek():
#     if isEmpty() : print("Queue_Empty")
#     else: return Q[fron+1]

