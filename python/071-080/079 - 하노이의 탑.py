def solution(n, start=1, to=3, via=2):
    result = []

    if n == 1:
        return [[start, to]]
    else:
        result.extend(solution(n - 1, start, via, to))
        result.append([start, to])
        result.extend(solution(n - 1, via, to, start))

    return result
