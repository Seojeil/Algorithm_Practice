# 햄버거 만들기


def solution(ingredient):
    answer = 0
    n = []

    for i in ingredient[:]:
        n.append(i)
        if n[-4:] == [1, 2, 3, 1]:
            del n[-4:]
            answer += 1

    return answer
