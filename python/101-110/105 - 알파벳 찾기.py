word = input()


def solution(s):
    dict_alpha = {
        "a": -1,
        "b": -1,
        "c": -1,
        "d": -1,
        "e": -1,
        "f": -1,
        "g": -1,
        "h": -1,
        "i": -1,
        "j": -1,
        "k": -1,
        "l": -1,
        "m": -1,
        "n": -1,
        "o": -1,
        "p": -1,
        "q": -1,
        "r": -1,
        "s": -1,
        "t": -1,
        "u": -1,
        "v": -1,
        "w": -1,
        "x": -1,
        "y": -1,
        "z": -1,
    }

    for alpha in dict_alpha.keys():
        index = s.find(alpha)
        dict_alpha[alpha] = index

    answer = []

    for index in dict_alpha.values():
        answer.append(str(index))

    answer = " ".join(answer)

    return answer


print(solution(word))
