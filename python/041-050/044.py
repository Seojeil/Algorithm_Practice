# 피보나치 수


def solution(n):
    F0 = 0
    F1 = 1

    while n > 1:
        F0, F1 = F1, F0 + F1
        n -= 1

    return F1 % 1234567
