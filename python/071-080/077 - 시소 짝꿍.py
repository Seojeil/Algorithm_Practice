def solution(weights):
    answer = 0

    ratio = [2 / 3, 3 / 4, 2 / 4, 3 / 2, 4 / 3, 4 / 2]

    count_weights = {key: 0 for key in weights}

    for weight in weights:
        count_weights[weight] += 1

    for weight_1 in count_weights:
        for weight_2 in count_weights:

            if weight_1 < weight_2:
                weight = weight_1 / weight_2

                if weight in ratio:
                    answer += count_weights[weight_1] * count_weights[weight_2]

            elif weight_1 == weight_2:
                answer += count_weights[weight_1] // 2

    return answer
