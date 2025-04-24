def solution(priorities, location):
    answer = 0
    queue = [(i, p) for i, p in enumerate(priorities)]

    while queue:
        if queue[0][1] < max([q[1] for q in queue]):
            queue = queue[1:] + [queue[0]]
        else:
            if queue[0][0] == location:
                answer += 1
                break

            queue = queue[1:]
            answer += 1

    return answer
