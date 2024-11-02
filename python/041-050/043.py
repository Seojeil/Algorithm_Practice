# JadenCase 문자열 만들기


def solution(s):
    answer = ""
    capitalize_next = True

    for char in s:
        if char == " ":
            capitalize_next = True
            answer += char
        elif char.isdigit():
            capitalize_next = False
            answer += char
        elif capitalize_next:
            answer += char.upper()
            capitalize_next = False
        else:
            answer += char.lower()
            capitalize_next = False
    return answer
