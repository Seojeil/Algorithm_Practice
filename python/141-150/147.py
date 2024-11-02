# 미로1

from collections import deque


def bfs(x, y):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    explore = deque()

    explore.append((x, y))
    maze[x][y] = 1
    while explore:
        x, y = explore.popleft()
        if maze[x][y] == 3:
            return 1
        maze[x][y] = 1
        for delta in range(4):
            visit_x, visit_y = x + dx[delta], y + dy[delta]
            if (
                0 <= visit_x < len(maze)
                and 0 <= visit_y < len(maze)
                and maze[visit_x][visit_y] != 1
            ):
                explore.append((visit_x, visit_y))
    return 0


for _ in range(10):
    testcase = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    x, y = 1, 1

    print(f"#{testcase}", bfs(x, y))
