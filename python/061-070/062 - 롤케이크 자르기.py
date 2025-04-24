def solution(topping):
    answer = 0

    forward = set()
    backward = {}

    for t in topping:
        backward[str(t)] = backward.get(str(t), 0)
        backward[str(t)] += 1

    for t in topping:
        forward.add(t)
        backward[str(t)] -= 1
        if backward[str(t)] == 0:
            del backward[str(t)]
        if len(forward) == len(backward):
            answer += 1

    return answer
