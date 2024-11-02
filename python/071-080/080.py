# 미로 탈출


def bfs(maps, x, y, to):
    delta_x, delta_y = [-1, 1, 0, 0], [0, 0, -1, 1]
    explore = [(x, y, 0)]
    visit = [(x, y)]

    while explore:
        current_x, current_y, current_d = explore.pop(0)

        if maps[current_y][current_x] == to:
            return current_d

        for d in range(4):
            new_x = current_x + delta_x[d]
            new_y = current_y + delta_y[d]
            if (
                0 <= new_x < len(maps[0])
                and 0 <= new_y < len(maps)
                and maps[new_y][new_x] != "X"
                and (new_x, new_y) not in visit
            ):
                explore.append((new_x, new_y, current_d + 1))
                visit.append((new_x, new_y))

    return -1


def solution(maps):
    for i, m in enumerate(maps):
        if "S" in m:
            s_x, s_y = (m.find("S"), i)
        if "L" in m:
            l_x, l_y = (m.find("L"), i)

    distance_s_to_l = bfs(maps, s_x, s_y, "L")
    distance_l_to_e = bfs(maps, l_x, l_y, "E")

    if distance_s_to_l == -1 or distance_l_to_e == -1:
        return -1
    else:
        return distance_s_to_l + distance_l_to_e
