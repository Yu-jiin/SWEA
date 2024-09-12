# W 로 시작하냐 B로 시작하냐 두 개 해서 개수 비교 할까
def start_white():
    white_count = 0

    for row in board:
        print(row[0])



def start_black():
    pass


N, M = map(int, input().split())
board = [list(map(str, input())) for _ in range(N)]

white_count = start_white()
black_count = start_black()

result = min(white_count,black_count)

print(result)
