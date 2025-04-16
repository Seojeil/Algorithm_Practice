# 초심자의 회문 검사


T = int(input())

for test_case in range(1, T + 1):
    text = input()

    if text == text[::-1]:
        answer = 1
    else:
        answer = 0

    print(f"#{test_case} {answer}")
