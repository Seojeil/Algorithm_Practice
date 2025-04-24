def solution(brown, yellow):

    x = ((brown + 4) / 2 + (((brown + 4) / 2) ** 2 - 4 * (brown + yellow)) ** 0.5) / 2
    y = ((brown + 4) / 2 - (((brown + 4) / 2) ** 2 - 4 * (brown + yellow)) ** 0.5) / 2

    return [x, y]
