# 구슬 탈출 1


from collections import deque

N, M = map(int, input().split())

board = []
red = ()
blue = ()

for i in range(N):
    row = list(input())

    for j, value in enumerate(row):
        if value == "R":
            red = (j, i)
            row[j] = "."
        if value == "B":
            blue = (j, i)
            row[j] = "."

    board.append(row)


def game(red, blue):
    beads = deque()
    beads.append((red, blue, 0))
    visited = set()
    visited.add((red, blue))

    next_beads = deque()

    while beads:
        cur_red, cur_blue, cur_count = beads.popleft()

        next_red, next_blue, next_count = left(cur_red, cur_blue, cur_count)
        next_beads.append((next_red, next_blue, next_count))

        next_red, next_blue, next_count = right(cur_red, cur_blue, cur_count)
        next_beads.append((next_red, next_blue, next_count))

        next_red, next_blue, next_count = up(cur_red, cur_blue, cur_count)
        next_beads.append((next_red, next_blue, next_count))

        next_red, next_blue, next_count = down(cur_red, cur_blue, cur_count)
        next_beads.append((next_red, next_blue, next_count))

        while next_beads:
            r, b, c = next_beads.popleft()

            if r == (-1, -1) and b != (-1, -1):
                return 1

            if (r, b) not in visited and b != (-1, -1) and c < 10:
                beads.append((r, b, c))
                visited.add((r, b))

    return 0


def left(r, b, c):
    rx, ry = r
    bx, by = b

    if rx < bx:
        while True:
            rx -= 1

            if board[ry][rx] == "O":
                rx, ry = -1, -1
                break
            if board[ry][rx] == "#":
                rx += 1
                break

        while True:
            bx -= 1

            if bx == rx and by == ry:
                bx += 1
                break
            if board[by][bx] == "O":
                bx, by = -1, -1
                break
            if board[by][bx] == "#":
                bx += 1
                break

        return (rx, ry), (bx, by), c + 1

    else:
        while True:
            bx -= 1

            if board[by][bx] == "O":
                bx, by = -1, -1
                break
            if board[by][bx] == "#":
                bx += 1
                break

        while True:
            rx -= 1

            if rx == bx and ry == by:
                rx += 1
                break
            if board[ry][rx] == "O":
                rx, ry = -1, -1
                break
            if board[ry][rx] == "#":
                rx += 1
                break

        return (rx, ry), (bx, by), c + 1


def right(r, b, c):
    rx, ry = r
    bx, by = b

    if rx > bx:
        while True:
            rx += 1

            if board[ry][rx] == "O":
                rx, ry = -1, -1
                break
            if board[ry][rx] == "#":
                rx -= 1
                break

        while True:
            bx += 1

            if bx == rx and by == ry:
                bx -= 1
                break
            if board[by][bx] == "O":
                bx, by = -1, -1
                break
            if board[by][bx] == "#":
                bx -= 1
                break

        return (rx, ry), (bx, by), c + 1

    else:
        while True:
            bx += 1

            if board[by][bx] == "O":
                bx, by = -1, -1
                break
            if board[by][bx] == "#":
                bx -= 1
                break

        while True:
            rx += 1

            if rx == bx and ry == by:
                rx -= 1
                break
            if board[ry][rx] == "O":
                rx, ry = -1, -1
                break
            if board[ry][rx] == "#":
                rx -= 1
                break

        return (rx, ry), (bx, by), c + 1


def up(r, b, c):
    rx, ry = r
    bx, by = b

    if ry < by:
        while True:
            ry -= 1

            if board[ry][rx] == "O":
                rx, ry = -1, -1
                break
            if board[ry][rx] == "#":
                ry += 1
                break

        while True:
            by -= 1

            if bx == rx and by == ry:
                by += 1
                break
            if board[by][bx] == "O":
                bx, by = -1, -1
                break
            if board[by][bx] == "#":
                by += 1
                break

        return (rx, ry), (bx, by), c + 1

    else:
        while True:
            by -= 1

            if board[by][bx] == "O":
                bx, by = -1, -1
                break
            if board[by][bx] == "#":
                by += 1
                break

        while True:
            ry -= 1

            if rx == bx and ry == by:
                ry += 1
                break
            if board[ry][rx] == "O":
                rx, ry = -1, -1
                break
            if board[ry][rx] == "#":
                ry += 1
                break

        return (rx, ry), (bx, by), c + 1


def down(r, b, c):
    rx, ry = r
    bx, by = b

    if ry > by:
        while True:
            ry += 1

            if board[ry][rx] == "O":
                rx, ry = -1, -1
                break
            if board[ry][rx] == "#":
                ry -= 1
                break

        while True:
            by += 1

            if bx == rx and by == ry:
                by -= 1
                break
            if board[by][bx] == "O":
                bx, by = -1, -1
                break
            if board[by][bx] == "#":
                by -= 1
                break

        return (rx, ry), (bx, by), c + 1

    else:
        while True:
            by += 1

            if board[by][bx] == "O":
                bx, by = -1, -1
                break
            if board[by][bx] == "#":
                by -= 1
                break

        while True:
            ry += 1

            if rx == bx and ry == by:
                ry -= 1
                break
            if board[ry][rx] == "O":
                rx, ry = -1, -1
                break
            if board[ry][rx] == "#":
                ry -= 1
                break

        return (rx, ry), (bx, by), c + 1


print(game(red, blue))
