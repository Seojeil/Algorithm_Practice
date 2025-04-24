def solution(picks, minerals):
    answer = 0
    fatigue = [[0, 0, 0] for _ in range(len(minerals) // 5 + 1)]
    fatigue_rules = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]

    for i, v in enumerate(minerals):
        if v == "diamond":
            fatigue[i // 5][0] += 1
        elif v == "iron":
            fatigue[i // 5][1] += 1
        else:
            fatigue[i // 5][2] += 1

    fatigue = fatigue[: sum(picks)]
    fatigue.sort(key=lambda a: (a[0], a[1], a[2]))

    for i, pick in enumerate(picks):
        for _ in range(pick):
            if not fatigue:
                break

            mine = fatigue.pop()

            for j, m in enumerate(mine):
                answer += fatigue_rules[i][j] * m

    return answer
