def solution(s):
    answer = ""
    NUMBER_DICT = {
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

            if word in NUMBER_DICT:
                answer += NUMBER_DICT[word]
                word = ""

        else:
            answer += n

    return int(answer)
