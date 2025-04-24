def find_n(num):
    n = 0
    while True:
        n += 1
        if hail(num, n) == 1:
            return n


def hail(num, n):
    for _ in range(n):
        if num % 2 == 0:
            num = num / 2
        else:
            num = num * 3 + 1

    return num


def solution(k, ranges):
    answer = []
    n = find_n(k)
    integrate_function = []

    for i in range(n):
        y_1 = max(hail(k, i), hail(k, i + 1))
        y_2 = min(hail(k, i), hail(k, i + 1))
        integrate_function.append(y_2 + (y_1 - y_2) / 2)

    for r in ranges:
        a, b = r
        if a <= n + b:
            integral = sum(integrate_function[a : n + b])
        else:
            integral = -1

        answer.append(integral)

    return answer
