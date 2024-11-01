# 숫자 문자열과 영단어


def solution(s):
    answer = ""
    n_dict = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    word = ""

    for n in s:
        print(n)
        if n.isalpha():
            word += n

            if word in n_dict:
                answer += n_dict[word]
                word = ""

        else:
            answer += n

    return int(answer)
