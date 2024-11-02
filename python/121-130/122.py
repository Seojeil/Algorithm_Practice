# 유사 라임 게임

import sys
from collections import Counter

T = int(sys.stdin.readline())

for _ in range(T):
    n, L, F = map(int, sys.stdin.readline().split())
    W = list(sys.stdin.readline().split())
    rhyme = []
    result = 0

    for w in W:
        rhyme.append(w[-F:])

    rhyme = Counter(rhyme)

    for v in rhyme.values():
        result += v // 2

    print(result)
