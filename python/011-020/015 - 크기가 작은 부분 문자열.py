def solution(t, p):
    answer = 0

    for n in range(len(t) - len(p) + 1):
        if int(t[n : n + len(p)]) <= int(p):
            answer += 1

    return answer
