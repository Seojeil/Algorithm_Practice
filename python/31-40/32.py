# 체육복


def solution(n, lost, reserve):
    for l in lost[:]:
        if l in reserve:
            lost.remove(l)
            reserve.remove(l)

    for l in sorted(reserve[:]):
        if l - 1 in lost:
            lost.remove(l - 1)
        elif l + 1 in lost:
            lost.remove(l + 1)

    n -= len(lost)

    return n
