# 문자열의 거울상


T = int(input())

for test_case in range(1, T + 1):
    word = input()
    mirror_word = ""
    word = word[::-1]

    for w in word:
        if w == "b":
            mirror_word += "d"
        elif w == "d":
            mirror_word += "b"
        elif w == "p":
            mirror_word += "q"
        elif w == "q":
            mirror_word += "p"

    print(f"#{test_case} {mirror_word}")
