# 혼자 놀기의 달인


def bfs(graph, start):
    explore = [start]

    for node in explore:
        if graph[node] not in explore:
            explore.append(graph[node])

    return explore, len(explore)


def solution(cards):
    dict_cards = {i + 1: v for i, v in enumerate(cards)}
    group_1 = 0
    group_2 = 0
    explored_node = []

    for i in range(1, len(cards) + 1):
        if i not in explored_node:
            explored, number_node = bfs(dict_cards, i)
            explored_node.extend(explored)

            if number_node >= group_2:
                group_2 = number_node

                if number_node >= group_1:
                    group_2 = group_1
                    group_1 = number_node

    return group_1 * group_2
