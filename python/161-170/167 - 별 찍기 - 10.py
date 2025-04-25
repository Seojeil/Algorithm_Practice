import sys

input = sys.stdin.readline


def drawing_stars(n):
    if n == 3:
        return [
            '***',
            '* *',
            '***'
            ]

    prev_pattern = drawing_stars(n//3)
    prev_size = n // 3

    new_pattern = []

    for line in prev_pattern:
        new_pattern.append(line*3)

    for line in prev_pattern:
        new_pattern.append(line + ' '*prev_size + line)

    for line in prev_pattern:
        new_pattern.append(line*3)

    return new_pattern


N = int(input())

result = drawing_stars(N)

for line in result:
    print(line)
