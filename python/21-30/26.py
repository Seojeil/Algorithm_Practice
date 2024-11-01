# 소수만들기


def is_prime(n):
    if n <= 1:
        return False

    if n % 2 == 0:
        return False

    i = 3

    while i**2 <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def solution(nums):
    answer = 0
    sums = []

    len_nums = len(nums)

    for n in range(len_nums):
        for k in range(n + 1, len_nums):
            for i in range(k + 1, len_nums):
                sums.append(nums[n] + nums[k] + nums[i])

    for n in sums:
        if is_prime(n):
            answer += 1

    return answer
