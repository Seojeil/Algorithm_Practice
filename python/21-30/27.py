# 덧칠하기


def solution(n, m, section):
    answer = 0
    n = 0

    for i in section:
        if i >= n:
            answer += 1
            n = i + m

    return answer
