# Ladder1


for test_case in range(1, 11):
    case_num = int(input())
    ladder = []

    for _ in range(100):
        numbers = list(map(int, input().split()))
        ladder.append(numbers)

    x = ladder[99].index(2)
    y = 99

    while y > 0:
        if x < 99 and ladder[y][x + 1] == 1:
            while ladder[y - 1][x + 1] == 0:
                x += 1
            x += 1
            y -= 1
        elif x > 0 and ladder[y][x - 1] == 1:
            while ladder[y - 1][x - 1] == 0:
                x -= 1
            x -= 1
            y -= 1
        elif ladder[y - 1][x] == 1:
            y -= 1

    print(f"#{test_case} {x}")
