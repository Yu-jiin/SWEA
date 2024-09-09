# W 로 시작하냐 B로 시작하냐 두 개 해서 개수 비교 할까
def start_white():
    pass


def start_black():
    pass


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

white_count = start_white(0)
black_count = start_black(0)

result = min(white_count,black_count)

print(result)