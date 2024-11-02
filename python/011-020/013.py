# 이상한 문자 만들기


def solution(s):
    answer = []

    words = s.split(" ")

    for word in words:
        new_word = ""

        for n in range(len(word)):
            if n % 2 == 0:
                new_word += word[n].upper()
            else:
                new_word += word[n].lower()

        answer.append(new_word)

    answer = " ".join(answer)

    return answer
