# 푸드 파이트 대회


def solution(food):
    answer = ""
    left = ""

    for n in range(1, len(food)):
        k = food[n] // 2
        left += k * str(n)

    answer = left + "0" + left[::-1]

    return answer
