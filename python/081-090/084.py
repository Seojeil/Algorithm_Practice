# 디펜스 게임


import heapq


def solution(n, k, enemy):
    max_heap = []
    l = len(enemy)

    for i in range(l):
        heapq.heappush(max_heap, enemy[i])
        if len(max_heap) > k:
            n -= heapq.heappop(max_heap)
        if n < 0:
            return i

    return l
