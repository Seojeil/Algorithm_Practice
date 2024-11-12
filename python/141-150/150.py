# 배달


def dijkstra(graph, start=1):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    explore = [(0, start)]

    while explore:
        distance, location = explore.pop(0)

        if distance > distances[location]:
            continue

        for node, node_distance in graph[location].items():
            expected_distance = node_distance + distance

            if expected_distance < distances[node]:
                distances[node] = expected_distance
                explore.append((expected_distance, node))

    return distances


def solution(N, road, K):
    answer = 0
    road_dict = {i: {} for i in range(1, N + 1)}

    for village, connect, distance in road:
        if connect in road_dict[village]:
            road_dict[village][connect] = min(distance, road_dict[village][connect])
            road_dict[connect][village] = min(distance, road_dict[connect][village])
        else:
            road_dict[village][connect] = distance
            road_dict[connect][village] = distance

    distances = dijkstra(road_dict)

    for distance in distances.values():
        if distance <= K:
            answer += 1

    return answer
