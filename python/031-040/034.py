# 대충 만든 자판


def solution(keymap, targets):
    answer = []

    for words in targets:
        n = 0

        for word in words:
            index = []

            for key in keymap:
                i = key.find(word)
                if i >= 0:
                    index.append(i + 1)

            if index != []:
                n += min(index)
            else:
                n = -1
                break

        answer.append(n)

    return answer
