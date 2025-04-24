def solution(babbling):
    BABY = ["aya", "ye", "woo", "ma"]

    for b in BABY:
        babbling = [x for x in babbling if b * 2 not in x]

    for b in BABY:
        babbling = [word.replace(b, " ") for word in babbling]

    for _ in babbling:
        babbling = [word.replace(" ", "") for word in babbling]

    answer = babbling.count("")

    return answer
