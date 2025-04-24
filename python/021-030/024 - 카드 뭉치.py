def solution(cards1, cards2, goal):
    goal2 = []

    for g in goal:
        if g in cards1:
            if g == cards1[0]:
                cards1 = cards1[(cards1.index(g)) + 1 :]
                goal2.append(g)
        elif g in cards2:
            if g == cards2[0]:
                cards2 = cards2[(cards2.index(g)) + 1 :]
                goal2.append(g)

    if goal2 == goal:
        answer = "Yes"
    else:
        answer = "No"

    return answer
