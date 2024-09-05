arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]

# 이진 트리 생성
nodes = [[] for _ in range(14)]
for i in range(0, len(arr), 2):
    parentNode = arr[i]
    childNode = arr[i + 1]
    nodes[parentNode].append(childNode)

# 자식이 없다는 걸 표현하기 위해 None 을 삽입
for li in nodes:
    for _ in range(len(li), 2):
        li.append(None)


# 전위 순회
def preorder(nodeNum):
    if nodeNum == None:
        return
    print(nodeNum, end = ' ')
    preorder(nodes[nodeNum][0])
    preorder(nodes[nodeNum][1])


preorder(1)

# 트리는 싸이클이 없는 무향 연결 그래프이다.
#  무향 - 방향이 없다 == 양방향
#   - 두 노드 사이에는 유일한 경로가 존재
#   - 최대 하나의 부모노드가 존재
#   - 자식노드가 없거나 하나 이상이 존재

#  사이클 - 뱅글뱅글 돌기

# 트리 코테 나오면 adjL
