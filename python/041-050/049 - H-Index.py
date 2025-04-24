def solution(citations):
    citations.sort(reverse=True)
    h = 0
    for i, n in enumerate(citations):
        if i < n:
            h = i + 1
        else:
            break

    return h
