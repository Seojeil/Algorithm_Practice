def solution(elements):
    answer = []

    for i in elements:
        cur_sum = i
        for j in elements[1:]:
            answer.append(cur_sum)
            cur_sum += j
        elements = elements[1:] + [elements[0]]

    return len(set(answer)) + 1
