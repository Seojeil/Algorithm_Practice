import sys


def dfs(w, h, M):
    explore = []
    result = 0

    for i in range(h):
        for j in range(w):
            if island_map[i][j] == 1:
                explore.append((j, i))
            else:
                continue

            while explore:
                x, y = explore.pop()
                island_map[y][x] = 0
                if x - 1 >= 0 and island_map[y][x - 1] == 1:
                    explore.append((x - 1, y))
                if y - 1 >= 0 and island_map[y - 1][x] == 1:
                    explore.append((x, y - 1))
                if x + 1 < w and island_map[y][x + 1] == 1:
                    explore.append((x + 1, y))
                if y + 1 < h and island_map[y + 1][x] == 1:
                    explore.append((x, y + 1))
                if x - 1 >= 0 and y - 1 >= 0 and island_map[y - 1][x - 1] == 1:
                    explore.append((x - 1, y - 1))
                if x - 1 >= 0 and y + 1 < h and island_map[y + 1][x - 1] == 1:
                    explore.append((x - 1, y + 1))
                if x + 1 < w and y - 1 >= 0 and island_map[y - 1][x + 1] == 1:
                    explore.append((x + 1, y - 1))
                if x + 1 < w and y + 1 < h and island_map[y + 1][x + 1] == 1:
                    explore.append((x + 1, y + 1))
            result += 1

    return result


while True:
    w, h = map(int, sys.stdin.readline().split())

    if w == 0 and h == 0:
        break

    island_map = []

    for _ in range(h):
        island_map.append(list(map(int, input().split())))

    print(dfs(w, h, island_map))
