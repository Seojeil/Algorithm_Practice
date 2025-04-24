from collections import deque


def solution(deck):
    deck = deque(deck)

    while len(deck) > 1:
        deck.popleft()
        n = deck.popleft()
        deck.append(n)

    result = deck.popleft()

    return result


N = int(input())

deck = sorted(list(range(1, N+1)))

print(solution(deck))
