Stack_Size = 10
stack = [0] * Stack_Size
top = -1

top += 1    # push(1)
stack[top] = 1
top += 1    # push(1)
stack[top] = 2
top += 1    # push(1)
stack[top] = 3

top -= 1
print(stack[top+1])
print(stack[top])

top -= 1
print(stack[top])
top -= 1
