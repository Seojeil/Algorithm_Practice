def check(r, c, place):
    if r - 1 >= 0 and place[c][r - 1] == "P":
        return False
    if r - 2 >= 0 and place[c][r - 2] == "P" and place[c][r - 1] != "X":
        return False
    if r + 1 < 5 and place[c][r + 1] == "P":
        return False
    if r + 2 < 5 and place[c][r + 2] == "P" and place[c][r + 1] != "X":
        return False
    if c - 1 >= 0 and place[c - 1][r] == "P":
        return False
    if c - 2 >= 0 and place[c - 2][r] == "P" and place[c - 1][r] != "X":
        return False
    if c + 1 < 5 and place[c + 1][r] == "P":
        return False
    if c + 2 < 5 and place[c + 2][r] == "P" and place[c + 1][r] != "X":
        return False
    if (
        r - 1 >= 0
        and c - 1 >= 0
        and place[c - 1][r - 1] == "P"
        and (place[c - 1][r] != "X" or place[c][r - 1] != "X")
    ):
        return False
    if (
        r - 1 >= 0
        and c + 1 < 5
        and place[c + 1][r - 1] == "P"
        and (place[c + 1][r] != "X" or place[c][r - 1] != "X")
    ):
        return False
    if (
        r + 1 < 5
        and c - 1 >= 0
        and place[c - 1][r + 1] == "P"
        and (place[c - 1][r] != "X" or place[c][r + 1] != "X")
    ):
        return False
    if (
        r + 1 < 5
        and c + 1 < 5
        and place[c + 1][r + 1] == "P"
        and (place[c + 1][r] != "X" or place[c][r + 1] != "X")
    ):
        return False
    return True


def solution(places):
    result = []

    for place in places:
        answer = []

        for cols in range(5):
            for rows in range(5):
                if place[cols][rows] == "P":
                    answer.append(check(rows, cols, place))

        result.append(1 if all(answer) else 0)

    return result
