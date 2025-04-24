T = int(input())

for test_case in range(1, T + 1):
    number = int(input())
    answer = 0

    for n in range(1, number + 1):
        if n % 2 == 0:
            answer -= n
        else:
            answer += n

    print(f"#{test_case} {answer}")
