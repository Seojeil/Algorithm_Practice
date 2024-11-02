# 마법의 엘레베이터


def solution(storey):
    answer = 0

    while storey > 0:
        a = storey % 10

        if a > 5:
            answer += 10 - a
            storey += 10
        elif a == 5 and (storey // 10) % 10 >= 5:
            answer += a
            storey += 10
        else:
            answer += a

        storey = storey // 10

    return answer
