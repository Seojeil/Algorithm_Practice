# 최대공약수와 최소공배수


def solution(n, m):
    if n >= m:
        a = n
        b = m
    else:
        a = m
        b = n

    while b != 0:
        a, b = b, a % b

    answer = [a, n * m / a]

    return answer