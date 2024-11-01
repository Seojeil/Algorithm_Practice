# 약수의 갯수
def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
    return count


# 소수 판별
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


# 원소의 빈도수
def count(string):
    result = {}

    for char in string:
        if char not in result:
            result[char] = 1
        else:
            result[char] += 1

    return result
