def solution(s, skip, index):
    ALPHA = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    answer = ""

    alpha = [i for i in ALPHA if i not in skip]
    seq = []

    for i in s:
        n = alpha.index(i)
        seq.append(n + index)

    for i in seq:
        answer += alpha[i % len(alpha)]

    return answer
