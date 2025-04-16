# 더하기


import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

even = 0
odd = 0

for a in range(N):
    if a % 2 == 0:
        odd += A[a]
    else:
        even += A[a]

if N == 3 and odd > even:
    result = -1
else:
    result = abs(odd - even)

print(result)
