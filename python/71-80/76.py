# 멀쩡한 사각형


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def solution(w, h):
    a = gcd(w, h)

    k = w // a + h // a - 1

    return w * h - k * a
