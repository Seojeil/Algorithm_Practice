def solution(n):
    answer = 0
    tri = []

    while n != 0:
        n, remainder = divmod(n, 3)
        tri.append(remainder)

    for k in range(len(tri), 0, -1):
        answer += tri[len(tri) - k] * (3 ** (k - 1))

    return answer
