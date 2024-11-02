# 의상


def solution(clothes):
    count_cloth = {}
    answer = 1
    for cloth in clothes:
        key = cloth[1]

        if key in count_cloth:
            count_cloth[key] += 1
        else:
            count_cloth[key] = 2

    for c in count_cloth.values():
        answer *= c

    return answer - 1
