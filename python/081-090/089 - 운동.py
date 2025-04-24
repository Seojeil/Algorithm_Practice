import sys

N, m, M, T, R = map(int, sys.stdin.readline().split())

result = 0

start = m

while N:
    if m + T > M and result == 0:
        result = -1
        break
    result += 1
    if m + T <= M:
        m += T
        N -= 1
        continue
    m -= R
    if m < start:
        m = start

print(result)
