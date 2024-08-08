def make_postfix(postfix):
    result = ''
    stack = []
    t = {
        '+': 1
    }
    for n in postfix:
        if n.isdigit():
            result + n
        elif n 


    return result

T = 10
for tc in range(1, T+1):
    str_len = int(input())
    postfix = list(map(str,input()))

    make_postfix(postfix)
