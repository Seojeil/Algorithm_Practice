import sys


def F(n):
    result = ""
    n = str(n)
    for k in n:
        result += str(9 - int(k))

    return int(result)


t = int(sys.stdin.readline())


def solution(N):
    l = len(str(N))

    if N < (10**l) // 2:
        result = N * F(N)
    else:
        N = (10**l) // 2
        result = N * F(N)

    return result


for _ in range(t):
    n = int(sys.stdin.readline())

    print(solution(n))
