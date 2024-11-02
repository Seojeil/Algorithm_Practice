# 로또의 최고순위와 최저순위


def solution(lottos, win_nums):
    answer = []
    cor = 0

    RANKING = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}

    for lotto in lottos:
        if lotto in win_nums:
            cor += 1

    zero = lottos.count(0)

    answer.append(RANKING[zero + cor])
    answer.append(RANKING[cor])

    return answer
