# 평균값 구하기


T = int(input())

for test_case in range(1, T + 1):
    numbers = list(map(int, input().split()))
    answer = 0
    len_number = 0

    for number in numbers:
        answer += number
        len_number += 1

    answer /= len_number

    print(f"#{test_case} {round(answer)}")
