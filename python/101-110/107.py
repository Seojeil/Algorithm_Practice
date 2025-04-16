# 친구 친구


import sys

n, m = map(int, sys.stdin.readline().split())

friends = {i: 0 for i in range(1, n + 1)}

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    friends[a] += 1
    friends[b] += 1

for v in friends.values():
    print(v)
