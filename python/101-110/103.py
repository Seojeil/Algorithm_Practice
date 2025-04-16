# 유레카 이론


import sys
from itertools import combinations_with_replacement


def tri(n):
    return n * (n + 1) // 2


t = int(sys.stdin.readline())

for _ in range(t):
    result = 0
    com_list = []
    k = int(sys.stdin.readline())

    for i in range(1, k + 1):
        if tri(i) >= k:
            com_list = list(combinations_with_replacement(range(1, i + 1), 3))
            break

    for a, b, c in com_list:
        if tri(a) + tri(b) + tri(c) == k:
            result = 1
            break

    print(result)
