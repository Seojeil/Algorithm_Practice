T = int(input())

for test_case in range(1, T + 1):
    repeat_word = input()
    answer = 1

    for l in range(1, len(repeat_word)):
        if repeat_word[:l] != repeat_word[l : l * 2]:
            answer += 1
        else:
            break

    print(f"#{test_case} {answer}")
