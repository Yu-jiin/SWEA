# 11~33까지 출력 1,2,3으로만

# for i in range(1,4):
#     for j in range(1,4):
#         print(f'{i}{j}')

# 1111~3333까지 출력 하려면
# 위에서 for 두번 더 쓰면 됨 !!

# 그러면 1111111111111~3333333333333은 반복문 저만치 쓸래 ?
# 좋은말로 할 때 재귀로
path = []
N = 3


def run(lev):
    if lev == N:
        print(path)
        return

    for i in range(1, 4):
        path.append(i)
        run(lev+1)
        path.pop()


run(0)

#  값만 복사,
#  함수가 끝나면, Main으로 돌아오는 것이 아닌 해당 함수를 호출했던 곳으로 돌아옴


