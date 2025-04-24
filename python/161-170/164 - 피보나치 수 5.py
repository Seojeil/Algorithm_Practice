import sys

input = sys.stdin.readline

N = int(input())


def fibonacci(num):
    if num == 1:
        return 1

    if num == 0:
        return 0

    return fibonacci(num - 1) + fibonacci(num - 2)


print(fibonacci(N))
