T = int(input())
for test_case in range(1, T + 1):
    l = int(input())
    arr = []

    for _ in range(l):
        numbers = list(map(int, input().split()))
        arr.append(numbers)

    arr_roll_90 = [[0] * l for _ in range(l)]
    arr_roll_180 = [[0] * l for _ in range(l)]
    arr_roll_270 = [[0] * l for _ in range(l)]

    for row in range(l):
        for col in range(l):
            arr_roll_90[row][col] = arr[l - 1 - col][row]

    for row in range(l):
        for col in range(l):
            arr_roll_180[row][col] = arr[l - 1 - row][l - 1 - col]

    for row in range(l):
        for col in range(l):
            arr_roll_270[row][col] = arr[col][l - 1 - row]

    print(f"#{test_case}")
    for n in range(l):
        print(
            "".join(map(str, arr_roll_90[n])),
            "".join(map(str, arr_roll_180[n])),
            "".join(map(str, arr_roll_270[n])),
        )
