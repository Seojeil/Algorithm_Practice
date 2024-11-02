# 리코쳇 로봇


def bfs(board, robot):
    delta_x, delta_y = [-1, 1, 0, 0], [0, 0, -1, 1]
    x, y = robot
    explored = set()
    explored.add((robot))
    explore = []
    explore.append((x, y, 0))

    while explore:
        x, y, c = explore.pop(0)
        if board[y][x] == "G":
            return c

        for d in range(4):
            cur_x, cur_y = x, y

            while True:
                cur_x += delta_x[d]
                cur_y += delta_y[d]

                if (
                    cur_x < 0
                    or cur_x >= len(board[0])
                    or cur_y < 0
                    or cur_y >= len(board)
                    or board[cur_y][cur_x] == "D"
                ):
                    cur_x -= delta_x[d]
                    cur_y -= delta_y[d]
                    break

            if (cur_x, cur_y) not in explored:
                explored.add((cur_x, cur_y))
                explore.append((cur_x, cur_y, c + 1))

    return -1


def solution(board):
    for i, b in enumerate(board):
        if "R" in b:
            robot = (b.index("R"), i)
            break

    return bfs(board, robot)
