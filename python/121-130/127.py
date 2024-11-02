# 자동차 주차


def pec(n):
    if n <= 1:
        return 1
    return n * pec(n - 1)


n, a, b, c = map(int, input().split())

print(pec(n) // (pec(a) * pec(b) * pec(c)))
