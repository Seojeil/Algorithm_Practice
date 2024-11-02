# 소수 찾기

import itertools


def id_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    sqrt_n = int(n**0.5)
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    perms = []
    answer = 0

    for i in range(1, len(numbers) + 1):
        current_perms = itertools.permutations(numbers, i)
        perms.extend([int("".join(map(str, perm))) for perm in current_perms])

    perms = list(set(perms))

    for perm in perms:
        if id_prime(perm):
            answer += 1

    return answer
