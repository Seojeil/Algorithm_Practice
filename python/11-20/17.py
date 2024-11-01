# 시저 암호


def solution(s, n):
    answer = ""

    for word in s:
        if word.isalpha():
            if word.islower():
                shifted = chr((ord(word) - ord("a") + n) % 26 + ord("a"))
            else:
                shifted = chr((ord(word) - ord("A") + n) % 26 + ord("A"))
            answer += shifted
        else:
            answer += word

    return answer
