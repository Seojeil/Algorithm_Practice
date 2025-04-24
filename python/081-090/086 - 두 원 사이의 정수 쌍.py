def solution(r1, r2):
    answer = 0

    for x in range(1, r2 + 1):
        print(x)
        max_y_r2 = int(((r2**2 - x**2) ** 0.5)) + 1
        min_y_r1 = (r1**2 - x**2) ** 0.5 if x < r1 else 0
        if min_y_r1 > int(min_y_r1):
            min_y_r1 = int(min_y_r1) + 1
        else:
            min_y_r1 = int(min_y_r1)
        print(max_y_r2, min_y_r1)

        answer += max_y_r2 - min_y_r1

    return answer * 4
