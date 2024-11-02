# 유기농 배추


def bfs(x, y, m, n):
    explore = []

    if field[y][x] != 1:
        return 0
    else:
        explore.append((x, y))
        field[y][x] = 0

        while explore:
            x, y = explore.pop(0)

            if x > 0 and field[y][x - 1] == 1:
                explore.append((x - 1, y))
                field[y][x - 1] = 0
            if y > 0 and field[y - 1][x] == 1:
                explore.append((x, y - 1))
                field[y - 1][x] = 0
            if x + 1 < m and field[y][x + 1] == 1:
                explore.append((x + 1, y))
                field[y][x + 1] = 0
            if y + 1 < n and field[y + 1][x] == 1:
                explore.append((x, y + 1))
                field[y + 1][x] = 0

        return 1


t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    field = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1

    result = 0

    for y in range(n):
        for x in range(m):
            result += bfs(x, y, m, n)

    print(result)
