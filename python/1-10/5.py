# 내적


def solution(a, b):
    answer = 0
    n = 1

    while n <= len(a):
        answer += a[n - 1] * b[n - 1]
        n += 1

    return answer
