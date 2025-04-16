# 토마토


import sys
from collections import deque


M, N = map(int, sys.stdin.readline().split())
box = []
tomato = deque()

for n in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    for m in range(M):
        if row[m] == 1:
            tomato.append((m, n))
    box.append(row)


def ripen(box, tomato, M, N):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    while tomato:
        x, y = tomato.popleft()

        for delta in range(4):
            visit_x, visit_y = x + dx[delta], y + dy[delta]
            if 0 <= visit_x < M and 0 <= visit_y < N and box[visit_y][visit_x] == 0:
                box[visit_y][visit_x] = box[y][x] + 1
                tomato.append((visit_x, visit_y))

    days = 0

    for row in box:
        for val in row:
            if val == 0:
                return -1
            days = max(days, val)

    return days - 1


print(ripen(box, tomato, M, N))
