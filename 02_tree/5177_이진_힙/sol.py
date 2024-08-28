import sys
sys.stdin = open('input.txt')

# 삽입을 위한 함수
# target : 삽입한 위치
def enqueue(target):
    #   단순히 tree에 삽입 대상을 집어 넣는게 아닌,
    #   삽입 후 부모 노드와 크기를 비교한 후
    #  부모노드의 값이 내 노드값보다 크다면 위치 스왑
    while target // 2:
        parent = target // 2
        if tree[target] <= tree[parent]:
            tree[target], tree[parent] = tree[parent], tree[target]
        target = parent


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    tree = [0]
    last_node = 0

    for item in arr:
        tree.append(item)
        last_node += 1
        enqueue(last_node)

    print(tree)
