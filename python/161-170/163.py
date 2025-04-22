# 팩토리얼 2


import sys

input = sys.stdin.readline

N = int(input())


def factorial(num):
    if num == 0:
        return 1

    return num * factorial(num-1)


print(factorial(N))
