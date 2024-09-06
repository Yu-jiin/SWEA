import sys
sys.stdin = open('1952.txt', 'r')


def dfs(month, sum_money):
    global result

    if month > 12:
        result = min(result, sum_money)
        return

    # 1일권
    dfs(month + 1, sum_money + (arr[month] * day1))
    # 한달권
    dfs(month + 1, sum_money + month1)
    # 세달권
    dfs(month + 3, sum_money + month3)


T = int(input())
for tc in range(1, T+1):
    money = list(map(int, input().split()))
    arr = [0] + list(map(int, input().split()))

    result = 1000000000000000

    day1 = money[0]         # 하루
    month1 = money[1]       # 한달
    month3 = money[2]       # 세달
    year = money[3]         # 1년

    dfs(1,0)

    if result > year:
        print(f'#{tc} {year}')
    else:
        print(f'#{tc} {result}')

