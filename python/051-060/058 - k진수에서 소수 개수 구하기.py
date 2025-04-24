def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    sqrt_n = int(n**0.5)

    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False

    return True


def solution(n, k):
    answer = 0
    prime_number = ""

    while n > 0:
        remainder = n % k
        prime_number = str(remainder) + prime_number
        n //= k

    number = prime_number.split("0")
    number = [int(s) for s in number if s.isdigit()]

    for num in number:
        if is_prime(num):
            answer += 1

    return answer
