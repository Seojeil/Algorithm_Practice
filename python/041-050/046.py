# 귤 고르기


def solution(k, tangerine):
    cou = {}
    answer = 0

    for t in tangerine:
        if t in cou:
            cou[t] += 1
        else:
            cou[t] = 1

    sortcou = sorted(cou.values(), reverse=True)

    n = 0
    while n < k:
        n += sortcou[answer]
        answer += 1

    return answer
