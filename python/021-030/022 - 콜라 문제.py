def solution(a, b, n):
    answer = 0
    rest = 0

    while n >= a:
        answer += (n // a) * b
        rest = n % a
        n = (n // a) * b
        n += int(rest)

    return answer
