# 삼각 달팽이


def solution(n):
    triangle = [[0] * i for i in range(1, n + 1)]

    num = 1
    x = -1
    y = 0

    for i in range(n):
        for _ in range(n - i):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            triangle[x][y] = num
            num += 1

    answer = []
    for row in triangle:
        answer.extend(row)

    return answer


print(solution(4))
