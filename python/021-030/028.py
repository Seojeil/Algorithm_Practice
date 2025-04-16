# 기사단원의 무기


def solution(number, limit, power):
    answer = 0

    for knight in range(1, number + 1):
        n = 0

        for k in range(1, int(knight**0.5) + 1):
            if knight % k == 0:
                if k * k != knight:
                    n += 2
                else:
                    n += 1

        if n > limit:
            answer += power
        else:
            answer += n

    return answer
