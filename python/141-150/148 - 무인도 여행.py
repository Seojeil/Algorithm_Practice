from collections import deque


def bfs(w, h, maps):
    explore = deque()
    explore.append((w, h))
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    food = int(maps[h][w])
    maps[h][w] = "X"

    while explore:
        x, y = explore.popleft()

        for d in direction:
            dx, dy = d

            if (
                0 <= x + dx < len(maps[0])
                and 0 <= y + dy < len(maps)
                and maps[y + dy][x + dx] != "X"
            ):
                explore.append((x + dx, y + dy))
                food += int(maps[y + dy][x + dx])
                maps[y + dy][x + dx] = "X"

    return food


def solution(maps):
    answer = []
    w = len(maps[0])
    h = len(maps)
    maps_list = [list(row) for row in maps]

    for i in range(h):
        for j in range(w):
            if maps_list[i][j] == "X":
                continue
            else:
                food = bfs(j, i, maps_list)
                answer.append(food)

    if not answer:
        return [-1]
    else:
        answer.sort()
        return answer


maps = ["XXX", "XXX", "XXX"]

print(solution(maps))
