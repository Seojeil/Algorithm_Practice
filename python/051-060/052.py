# 할인 행사


def solution(want, number, discount):
    answer = 0
    i = 0

    while i <= len(discount) - 10:
        want_dictionary = dict(zip(want, number))

        for product in discount[i : 10 + i]:
            if product in want_dictionary:
                want_dictionary[product] -= 1

                if want_dictionary[product] == 0:
                    want_dictionary.pop(product)

        if want_dictionary == {}:
            answer += 1

        i += 1

    return answer
