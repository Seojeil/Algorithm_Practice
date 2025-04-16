# DFS와 BFS


import copy


def dfs(tree, n, start, result=None):
    if result is None:
        result = []

    result.append(start)

    while len(result) < n:
        if start not in tree or not tree[start]:
            break

        node = tree[start].pop(0)

        if node not in result:
            dfs(tree, n, node, result)

    return result


def bfs(tree, n, start, result=None):
    if result is None:
        result = []

    result.append(start)

    for s in result:
        if len(result) >= n:
            break

        while tree[s]:
            if tree[s][0] not in result:
                k = tree[s].pop(0)
                result.append(k)
            else:
                tree[s].pop(0)

    return result


n, m, start = map(int, input().split())

tree = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

for key in tree:
    tree[key].sort()

tree_2 = copy.deepcopy(tree)

t_1 = dfs(tree, n, start)
t_2 = bfs(tree_2, n, start)

tt_1 = " ".join(map(str, t_1))
tt_2 = " ".join(map(str, t_2))

print(tt_1)
print(tt_2)
