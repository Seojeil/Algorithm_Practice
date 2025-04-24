def solution(s):
    answer = []
    dup = []

    for word in s:
        if word not in dup:
            answer.append(-1)
            dup.append(word)
        else:
            i = dup[::-1].index(word)
            answer.append(i + 1)
            dup.append(word)

    return answer
