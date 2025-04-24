from functools import reduce


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def solution(arrayA, arrayB):
    result_a = 0
    result_b = 0

    gcd_a = reduce(gcd, arrayA)
    gcd_b = reduce(gcd, arrayB)

    divisor_a = []
    divisor_b = []

    for a in range(1, gcd_a + 1):
        if gcd_a % a == 0:
            divisor_a.append(a)
    for b in range(1, gcd_b + 1):
        if gcd_b % b == 0:
            divisor_b.append(b)

    while divisor_a:
        k = divisor_a.pop()
        for arr_b in arrayB:
            if arr_b % k == 0:
                break
        else:
            result_a = k
        break

    while divisor_b:
        k = divisor_b.pop()
        for arr_a in arrayA:
            if arr_a % k == 0:
                break
        else:
            result_b = k
        break

    return max(result_a, result_b)
