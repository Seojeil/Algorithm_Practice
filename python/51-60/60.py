# 모음사전


def solution(word):
    find_word = [0, 0, 0, 0, 0]
    index = [1, 0, 0, 0, 0]
    answer = 1

    for i, w in enumerate(word):
        if w == "A":
            find_word[i] = 1
        elif w == "E":
            find_word[i] = 2
        elif w == "I":
            find_word[i] = 3
        elif w == "O":
            find_word[i] = 4
        else:
            find_word[i] = 5

    if find_word == [1, 0, 0, 0, 0]:
        return 1

    while True:
        if 0 in index:
            i = index.index(0)
            index[i] += 1
            answer += 1
        else:
            index[4] += 1
            answer += 1

        while 6 in index:
            i = index.index(6)
            index[i] = 0
            index[i - 1] += 1

        if index == find_word:
            break

    return answer
