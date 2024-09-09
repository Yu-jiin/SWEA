'''
AABCDD
afzz
09121
a8EWg6
P5h3kx
'''

lst = [list(map(str, input())) for _ in range(5)]

max_row = 0
for row in lst:
    if max_row < len(row):
        max_row = len(row)

for row in lst:
    while len(row) < max_row:
        row.append('')

real = ''
answer = list(zip(*lst))
for row in answer:
    print(''.join(map(str, row)), end="")

