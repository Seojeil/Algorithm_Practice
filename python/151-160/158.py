# 약수


import sys

input = sys.stdin.readline

_ = int(input())
divisor = list(map(int, input().split()))

print(min(divisor) * max(divisor))
