# 전자레인지


import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
d = int(sys.stdin.readline())
e = int(sys.stdin.readline())


if a < 0:
    result = (-a) * c + d + b * e
else:
    result = (b - a) * e

print(result)
