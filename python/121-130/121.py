# 추첨상 사수 대작전! (Normal)

import sys

m, seed, x1, x2 = map(int, sys.stdin.readline().split())

for an in range(m):
    c = (x1 - an * seed) % m

    if x2 == (an * x1 + c) % m:
        a = an
        break

print(a, c)
