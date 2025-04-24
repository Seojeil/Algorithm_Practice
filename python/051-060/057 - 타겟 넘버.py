import itertools


def solution(numbers, target):
    answer = 0
    combinations = itertools.product([1, -1], repeat=len(numbers))

    for combination in combinations:
        sum_numbers = 0
        for i, c in enumerate(combination):
            sum_numbers += numbers[i] * c
        if sum_numbers == target:
            answer += 1

    return answer
