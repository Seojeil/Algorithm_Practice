T = int(input())

for test_case in range(1, T + 1):
    students, _ = map(int, input().split())
    task = list(map(int, input().split()))

    result = []

    for student in range(1, students + 1):
        if student not in task:
            result.append(student)

    result = " ".join([str(i) for i in result])

    print(f"#{test_case} {result}")
