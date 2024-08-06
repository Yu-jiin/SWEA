# 스택 삽입 시 append를 사용하면 느려지지만 단순하게는 좋음

def push(item, size):
    global top
    top += 1
    if top == size:
        print('overflow')
    else:
        stack[top] = item


size = 10
stack = [0] * size
top = -1

push(10, size)
top += 1
stack[top] = 20

s = [1, 0]
# pop 알고리즘
def my_pop():
    if len(s) == 0:
        # underflow
        return
    else:
        return s.pop()


def my_pop2():
    global top
    if top == -1:
        print('underflow')
        return 0
    else:
        top -= 1
        return stack[top+1]

# if top > -1:
#     top -= 1
#     print(stack[top+1])   print(stack[top])
#                           top -= 1


# 스택 괄호의 종류 : 대, 중, 소 괄호
#     조건 : 왼쪽 괄호의 개수, 오른쪽 괄호의 개수가 같아야함
#           같은 괄호에서 왼쪽이 오른쪽보다 먼저 나와야함
#           괄호 사이에는 포함관계만 존재한다.

# 스택에서의 삭제 = 꺼낸다
