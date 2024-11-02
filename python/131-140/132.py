T = int(input())

for test_case in range(1, T + 1):
    l, area = map(int, input().split())
    fly = []

    for _ in range(l):
        numbers = list(map(int, input().split()))
        fly.append(numbers)

    many = 0
    for col in range(l - area + 1):
        for row in range(l - area + 1):
            answer = 0

            for c in range(area):
                answer += sum(fly[col + c][row : row + area])

            many = max(answer, many)

    print(f"#{test_case} {many}")
