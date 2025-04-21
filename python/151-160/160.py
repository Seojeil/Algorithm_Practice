# 붙임성 좋은 총총이


import sys

input = sys.stdin.readline

N = int(input())

rainbow = {'ChongChong'}

for _ in range(N):
    name_1, name_2 = input().split()

    if name_1 in rainbow:
        rainbow.add(name_2)

    if name_2 in rainbow:
        rainbow.add(name_1)

print(len(rainbow))
