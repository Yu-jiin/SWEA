def find_set(node):
    if parent[node] != node:
        parent[node] = find_set(parent[node])
    return parent[node]


def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1


N = 5
parent = list(range(N))
rank = [1] * N

union(0, 1)
print(f'0과 1 결합 {parent} {rank}')
print(find_set(0))
print(find_set(1))
union(1, 2)
print(f'1과 2 결합 {parent} {rank}')