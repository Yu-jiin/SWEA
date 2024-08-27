import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [[] for _ in range(N+2)]

    lst1 = []
    lst2 = []
    for _ in range(N):
        arr = list(map(str, input().split()))
        lst1 = arr.pop(0)
        lst2.append(arr.pop(0))
        print(arr)
        a, b = int(arr[0]), int(arr[1])
        tree[a].append(b)
        for i in range(N+2):
            while len(tree[i+1]) < 2:
                tree[i+1].append(-1)

    print(tree)
    print(lst1)
    print(lst2)


    # for i in range(N+2):
    #     while len(tree[i]) < 2:
    #         tree[i].append(-1)

















    # def in_order(n):
    #     global word
    #     if n <= N:
    #         # 왼쪽 자식
    #         in_order(n * 2)
    #         # 알파벳
    #         word += arr[n - 1][1]
    #         # 오른쪽 자식
    #         in_order(n * 2 + 1)
    #
    #
    # for tc in range(1, 11):
    #     # 트리가 갖는 정점의 총 수
    #     N = int(input())
    #     # 정점 번호, 해당 정점 알파벳, 왼쪽 자식, 오른쪽 자식
    #     arr = [input().split() for _ in range(N)]
    #
    #     # 단어
    #     word = ''
    #     in_order(1)
    #     print(f'#{tc} {word}')
