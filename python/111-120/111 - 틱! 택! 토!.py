user = int(input())
com = 3 - user

board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
row_user = {1: 0, 2: 0, 3: 0}
col_user = {1: 0, 2: 0, 3: 0}
diagonal_user_1 = 0
diagonal_user_2 = 0
row_com = {1: 0, 2: 0, 3: 0}
col_com = {1: 0, 2: 0, 3: 0}
diagonal_com_1 = 0
diagonal_com_2 = 0
count = 0

while True:
    y, x = map(int, input().split())
    board[y - 1][x - 1] = user
    row_user[x] += 1
    col_user[y] += 1

    if x == y:
        diagonal_user_1 += 1

    if x + y == 4:
        diagonal_user_2 += 1

    if (
        diagonal_user_1 == 3
        or diagonal_user_2 == 3
        or row_user[x] == 3
        or col_user[y] == 3
    ):
        result = user
        break

    count += 1

    if count == 9:
        result = 0
        break

    y, x = map(int, input().split())
    board[y - 1][x - 1] = com
    row_com[x] += 1
    col_com[y] += 1

    if x == y:
        diagonal_com_1 += 1

    if x + y == 4:
        diagonal_com_2 += 1

    if diagonal_com_1 == 3 or diagonal_com_2 == 3 or row_com[x] == 3 or col_com[y] == 3:
        result = com
        break

    count += 1

print(result)
