# 숫자 변환하기

from collections import deque


def solution(x, y, n):
    if x == y:
        return 0

    queue = deque([(x, 0)])
    visited = set()
    visited.add(x)

    while queue:
        current, operations = queue.popleft()
        next_numbers = [current + n, current * 2, current * 3]

        for next_number in next_numbers:
            if next_number == y:
                return operations + 1
            if next_number < y and next_number not in visited:
                visited.add(next_number)
                queue.append((next_number, operations + 1))

    return -1
