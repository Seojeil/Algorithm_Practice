import sys

input = sys.stdin.readline


def Cantor(string, n):
    if n == 0:
        return string

    part_length = len(string) // 3

    first_part = Cantor(string[:part_length], n-1)

    middle_part = ' ' * part_length

    last_part = Cantor(string[2*part_length:], n-1)

    return first_part + middle_part + last_part


while True:
    try:
        N = int(input())
        string = '-' * (3 ** N)
        print(Cantor(string, N))

    except ValueError:
        break
