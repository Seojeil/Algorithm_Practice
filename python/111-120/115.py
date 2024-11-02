# 과일노리

import sys

N = int(sys.stdin.readline())

bot = {i: () for i in range(N)}

time = 0

for _ in range(N):
    a, b = tuple(map(int, sys.stdin.readline().split()))
    cycle = a + b
    second = time % cycle

    if second < b:
        time += b - second
    time += 1

print(time)
