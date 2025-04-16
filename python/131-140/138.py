# 달팽이 숫자


T = int(input())

for test_case in range(1, T + 1):
    snail_size = int(input())

    snail_house = [[0] * snail_size for _ in range(snail_size)]
    x, y = 0, 0
    move = "right"

    for snail in range(1, snail_size**2 + 1):
        snail_house[x][y] = snail
        if move == "right":
            if y + 1 < snail_size and snail_house[x][y + 1] == 0:
                y += 1
            else:
                move = "down"
                x += 1
        elif move == "down":
            if x + 1 < snail_size and snail_house[x + 1][y] == 0:
                x += 1
            else:
                move = "left"
                y -= 1
        elif move == "left":
            if y - 1 >= 0 and snail_house[x][y - 1] == 0:
                y -= 1
            else:
                move = "up"
                x -= 1
        elif move == "up":
            if x - 1 >= 0 and snail_house[x - 1][y] == 0:
                x -= 1
            else:
                move = "right"
                y += 1

    print(f"#{test_case}")

    for snail_move in snail_house:
        print(" ".join(map(str, snail_move)))
