import sys

_ = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

result = 0

for a in A:
    result = 1 - (1 - result) * (1 - a / 100.0)
    print(result * 100)
