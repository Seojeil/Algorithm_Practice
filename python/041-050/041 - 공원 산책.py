def solution(park, routes):
    for y in range(len(park)):
        if "S" in park[y]:
            x = park[y].index("S")
            robot = [y, x]
            break

    D = {"E": [0, 1], "W": [0, -1], "S": [1, 0], "N": [-1, 0]}

    for route in routes:
        direct, distance = route.split(" ")
        move_robot = robot[:]

        for _ in range(int(distance)):
            move_robot[0] += D[direct][0]
            move_robot[1] += D[direct][1]

            if (
                move_robot[0] >= len(park)
                or move_robot[0] < 0
                or move_robot[1] >= len(park[0])
                or move_robot[1] < 0
                or park[move_robot[0]][move_robot[1]] == "X"
            ):
                break

        else:
            robot = move_robot

    return robot
