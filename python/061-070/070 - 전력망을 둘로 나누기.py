def dfs(tree, n, node=1, count=1, explore=None):
    if explore is None:
        explore = []
    explore.append(node)

    while count < n:
        if not tree[node]:
            break
        next_node = tree[node].pop(0)
        if next_node not in explore:
            count = dfs(tree, n, next_node, count + 1, explore)

    return count


def solution(n, wires):
    answer = float("inf")

    for i in range(len(wires)):
        cut_wires = wires[:i] + wires[i + 1 :]
        dict_wires = {i: [] for i in range(1, n + 1)}

        for wire in cut_wires:
            dict_wires[wire[0]].append(wire[1])
            dict_wires[wire[1]].append(wire[0])
        answer = min(answer, abs(n - dfs(dict_wires, n) * 2))

        if answer == 0:
            break

    return answer
